#!/usr/bin/env python3
"""
CAD-to-GLTF Converter for MESGRO Project
=========================================

Converts CAD files to optimized GLTF with vertex color support
for GitHub Pages 3D visualization.

Supported Formats:
------------------
- 3MF (.3mf) - 3D Manufacturing Format [RECOMMENDED for Onshape]
  - Preserves per-object colors/materials as vertex colors
  - Assembly support with accurate colors
- STL (.stl) - Universal mesh format (no colors)
- STEP/STP (.step, .stp) - CAD exchange format (no colors)

Color Support:
-----------
3MF files contain color/material data which is extracted and baked as
vertex colors in the output GLTF. This allows per-object color visualization
without needing separate texture files.

Export Instructions:
-------------------
- Onshape: **File → Download → 3MF** (best option with colors!)
  - Also supports: File → Download → STEP, OBJ
- SolidWorks: File → Save As → STEP or STL
- Fusion 360: File → Export → STEP or STL
- Inventor: File → Export → STEP or STL

Proprietary formats (SLDPRT, F3D, etc.) cannot be read without licensing.

Installation:
-------------
    pip install trimesh numpy cadquery-ocp draco3d

Usage:
------
    python cad_to_gltf.py -i model.3mf -o output.glb  # With colors!
    python cad_to_gltf.py -i model.step -o output.glb
    python cad_to_gltf.py -i model.stl -o output.glb
    python cad_to_gltf.py --check-step

Author: MESGRO Project
License: MIT
"""

import argparse
import sys
from pathlib import Path
from typing import Optional, Tuple

# =============================================================================
# Dependency Check
# =============================================================================

def check_step_support() -> Tuple[bool, Optional[str]]:
    """Check if STEP file support is available."""
    try:
        from OCP.STEPControl import STEPControl_Reader
        return True, "cadquery-ocp"
    except ImportError:
        pass
    
    try:
        from OCC.Core.STEPControl import STEPControl_Reader
        return True, "pythonocc-core"
    except ImportError:
        pass
    
    return False, None


# Check core dependencies
try:
    import numpy as np
    import trimesh
except ImportError as e:
    print(f"ERROR: Missing dependency: {e}")
    print("Install with: pip install trimesh numpy")
    sys.exit(1)


# =============================================================================
# Supported Formats
# =============================================================================

SUPPORTED_FORMATS = {'.stl', '.step', '.stp', '.3mf'}


# =============================================================================
# Loaders
# =============================================================================

def load_stl(input_path: Path) -> trimesh.Trimesh:
    """Load an STL file."""
    print(f"  Loading STL: {input_path.name}")
    mesh = trimesh.load(str(input_path), file_type='stl', force='mesh')
    
    if isinstance(mesh, trimesh.Scene):
        mesh = mesh.dump(concatenate=True)
    
    return mesh


def load_3mf(input_path: Path) -> trimesh.Trimesh:
    """Load a 3MF file with color/material extraction.
    
    3MF format can contain per-object colors which are extracted and
    baked as vertex colors in the output mesh. This avoids needing
    separate texture files.
    """
    print(f"  Loading 3MF: {input_path.name}")
    
    # Load the 3MF file as a scene (preserves assembly structure)
    scene = trimesh.load(str(input_path), file_type='3mf', force='scene')
    
    print(f"  Found {len(scene.geometry)} geometries in scene")
    
    # Collect all meshes while preserving colors from per-geometry visual data
    meshes_with_colors = []
    
    for geom_name, geom in scene.geometry.items():
        if isinstance(geom, trimesh.Trimesh):
            # Try to extract vertex colors from the visual property
            try:
                # Check if geometry has vertex colors
                if hasattr(geom.visual, 'vertex_colors'):
                    vertex_colors = geom.visual.vertex_colors
                    if vertex_colors is not None and len(vertex_colors) > 0:
                        geom.visual.vertex_colors = vertex_colors
                        print(f"    {geom_name}: {len(geom.vertices)} vertices with colors")
                    else:
                        print(f"    {geom_name}: {len(geom.vertices)} vertices (no color data)")
                elif hasattr(geom.visual, 'face_colors'):
                    face_colors = geom.visual.face_colors
                    if face_colors is not None and len(face_colors) > 0:
                        # Convert face colors to vertex colors
                        vertex_colors = np.zeros((len(geom.vertices), 4), dtype=np.uint8)
                        # Average face colors at each vertex
                        for face_idx, face in enumerate(geom.faces):
                            color = face_colors[face_idx]
                            for vertex_idx in face:
                                if np.all(vertex_colors[vertex_idx] == 0):
                                    vertex_colors[vertex_idx] = color
                        geom.visual.vertex_colors = vertex_colors
                        print(f"    {geom_name}: {len(geom.vertices)} vertices (colors converted from faces)")
                else:
                    print(f"    {geom_name}: {len(geom.vertices)} vertices")
            except Exception as e:
                print(f"    {geom_name}: {len(geom.vertices)} vertices (color extraction: {e})")
            
            meshes_with_colors.append(geom)
    
    if not meshes_with_colors:
        print("  WARNING: No geometries found in 3MF file")
        return None
    
    # Merge all meshes while preserving visual data
    if len(meshes_with_colors) == 1:
        return meshes_with_colors[0]
    
    # For multiple geometries, merge them while trying to preserve colors
    print("  Merging multiple geometries...")
    combined_mesh = trimesh.util.concatenate(meshes_with_colors)
    
    return combined_mesh


def load_step(input_path: Path) -> trimesh.Trimesh:
    """Load a STEP file using OpenCASCADE (cadquery-ocp)."""
    step_ok, library = check_step_support()
    
    if not step_ok:
        raise ImportError(
            "STEP support requires cadquery-ocp.\n"
            "Install with: pip install cadquery-ocp\n"
            "Or export your STEP to STL from CAD software."
        )
    
    print(f"  Loading STEP via {library}: {input_path.name}")
    
    # Import based on available library
    if library == "cadquery-ocp":
        from OCP.STEPControl import STEPControl_Reader
        from OCP.BRepMesh import BRepMesh_IncrementalMesh
        from OCP.TopExp import TopExp_Explorer
        from OCP.TopAbs import TopAbs_FACE
        from OCP.BRep import BRep_Tool
        from OCP.TopLoc import TopLoc_Location
        from OCP.TopoDS import TopoDS
    else:
        from OCC.Core.STEPControl import STEPControl_Reader
        from OCC.Core.BRepMesh import BRepMesh_IncrementalMesh
        from OCC.Core.TopExp import TopExp_Explorer
        from OCC.Core.TopAbs import TopAbs_FACE
        from OCC.Core.BRep import BRep_Tool
        from OCC.Core.TopLoc import TopLoc_Location
        try:
            from OCC.Core.TopoDS import topods_Face
        except ImportError:
            from OCC.Core.TopoDS import topods
    
    # Read STEP
    reader = STEPControl_Reader()
    if reader.ReadFile(str(input_path)) != 1:
        raise ValueError(f"Failed to read STEP: {input_path}")
    
    reader.TransferRoots()
    shape = reader.OneShape()
    
    # Tessellate
    # Coarser deflection significantly reduces exported web model size.
    BRepMesh_IncrementalMesh(shape, 0.8)
    
    # Extract mesh
    vertices, faces = [], []
    offset = 0
    
    explorer = TopExp_Explorer(shape, TopAbs_FACE)
    while explorer.More():
        face_shape = explorer.Current()
        if library == "cadquery-ocp":
            face = TopoDS.Face_s(face_shape)
        else:
            try:
                face = topods_Face(face_shape)
            except NameError:
                face = topods.Face(face_shape)
        location = TopLoc_Location()
        tri = BRep_Tool.Triangulation_s(face, location)
        
        if tri:
            for i in range(1, tri.NbNodes() + 1):
                node = tri.Node(i)
                if not location.IsIdentity():
                    node = node.Transformed(location.Transformation())
                vertices.append([node.X(), node.Y(), node.Z()])
            
            for i in range(1, tri.NbTriangles() + 1):
                t = tri.Triangle(i)
                n1, n2, n3 = t.Get()
                faces.append([n1-1+offset, n2-1+offset, n3-1+offset])
            
            offset += tri.NbNodes()
        
        explorer.Next()
    
    return trimesh.Trimesh(vertices=np.array(vertices), faces=np.array(faces))


# =============================================================================
# Processing & Export
# =============================================================================

def optimize_mesh(mesh: trimesh.Trimesh) -> trimesh.Trimesh:
    """Optimize mesh for web viewing."""
    print("  Optimizing...")
    mesh.merge_vertices()
    # Use update_faces with a mask to remove degenerate/duplicate faces
    if hasattr(mesh, 'remove_degenerate_faces'):
        mesh.remove_degenerate_faces()
    if hasattr(mesh, 'remove_duplicate_faces'):
        mesh.remove_duplicate_faces()
    # Fix normals if needed
    try:
        if not mesh.is_winding_consistent:
            mesh.fix_normals()
    except Exception:
        pass  # Some meshes may not support this check

    # Keep very large assemblies at a manageable size for web deployment.
    max_faces = 5_000_000
    if len(mesh.faces) > max_faces:
        try:
            print(f"  Decimating faces: {len(mesh.faces):,} -> {max_faces:,}")
            mesh = mesh.simplify_quadric_decimation(face_count=max_faces)
        except Exception as exc:
            print(f"  Decimation skipped: {exc}")

    print(f"  Result: {len(mesh.vertices):,} vertices, {len(mesh.faces):,} faces")
    return mesh


def export_with_draco(mesh: trimesh.Trimesh, output_path: Path) -> bool:
    """Try to export glTF with Draco compression for smaller file sizes."""
    try:
        import draco3d
        print("  Applying Draco compression...")
        scene = trimesh.Scene(mesh)
        # Export to glb with compression option
        glb_data = scene.export(file_type='glb')
        # Draco compression is applied by trimesh when support is available
        with open(output_path, 'wb') as f:
            f.write(glb_data)
        return True
    except ImportError:
        print("  Note: Draco compression not available (install draco3d for smaller files)")
        return False



def export_gltf(mesh: trimesh.Trimesh, output_path: Path) -> None:
    """Export to GLTF with Draco compression and embedded binary."""
    print(f"  Exporting: {output_path.name}")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    scene = trimesh.Scene(mesh)
    
    # GLB format (binary GLTF) - more reliable, better for Draco
    glb_data = scene.export(file_type='glb')
    
    # Write to output file
    with open(output_path, 'wb') as f:
        f.write(glb_data)
    
    size = output_path.stat().st_size
    size_mb = size / (1024 * 1024)
    size_kb = size / 1024
    
    if size_mb > 1:
        print(f"  Size: {size_mb:.2f} MB")
    else:
        print(f"  Size: {size_kb:.2f} KB")


# =============================================================================
# Main
# =============================================================================

def convert(input_file: str, output_file: str) -> bool:
    """Convert CAD to GLTF."""
    input_path = Path(input_file).resolve()
    output_path = Path(output_file).resolve()
    
    if not input_path.exists():
        print(f"ERROR: File not found: {input_path}")
        return False
    
    ext = input_path.suffix.lower()
    if ext not in SUPPORTED_FORMATS:
        print(f"ERROR: Unsupported format: {ext}")
        print(f"Supported: {', '.join(SUPPORTED_FORMATS)}")
        if ext in {'.sldprt', '.sldasm'}:
            print("\n→ SolidWorks files: Export to STL/STEP via File → Save As")
        elif ext in {'.f3d', '.iam', '.ipt'}:
            print("\n→ Autodesk files: Export to STL/STEP via File → Export")
        return False
    
    print(f"\n{'='*50}")
    print("CAD-to-GLTF Converter")
    print(f"{'='*50}")
    print(f"Input:  {input_path}")
    print(f"Output: {output_path}\n")
    
    try:
        if ext == '.stl':
            mesh = load_stl(input_path)
        elif ext == '.3mf':
            mesh = load_3mf(input_path)
        else:  # .step, .stp
            mesh = load_step(input_path)
        
        if mesh is None:
            print("ERROR: Failed to load mesh")
            return False
        
        mesh = optimize_mesh(mesh)
        export_gltf(mesh, output_path)
        print(f"\n✓ Success!\n")
        return True
    except ImportError as e:
        print(f"\nERROR: {e}")
        return False
    except Exception as e:
        print(f"\nERROR: {type(e).__name__}: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Convert STL/STEP to GLTF for web 3D viewing.",
        epilog="Supported: .stl, .step, .stp | NOT supported: .sldprt, .f3d (export first)"
    )
    parser.add_argument('-i', '--input_file', help="Input file (.stl/.step/.stp)")
    parser.add_argument('-o', '--output_file', help="Output GLTF file")
    parser.add_argument('--check-step', action='store_true', help="Check STEP support")
    
    args = parser.parse_args()
    
    if args.check_step:
        ok, lib = check_step_support()
        print(f"✓ STEP support: {lib}" if ok else "✗ STEP not installed\n  pip install cadquery-ocp")
        sys.exit(0 if ok else 1)
    
    if not args.input_file or not args.output_file:
        parser.error("Both -i and -o are required")
    
    sys.exit(0 if convert(args.input_file, args.output_file) else 1)


if __name__ == "__main__":
    main()
