#!/usr/bin/env python3
"""Generate reduced GLB LODs from a source GLB using Blender decimation.

Usage:
  blender -b -P scripts/blender_gltf_lod.py -- input.glb output.glb ratio

Example:
  blender -b -P scripts/blender_gltf_lod.py -- in.glb out-medium.glb 0.55
"""

import os
import sys

import bpy


def parse_args() -> tuple[str, str, float]:
    if "--" not in sys.argv:
        raise SystemExit("Missing '--' before arguments")
    args = sys.argv[sys.argv.index("--") + 1 :]
    if len(args) != 3:
        raise SystemExit(
            "Usage: blender -b -P scripts/blender_gltf_lod.py -- input.glb output.glb ratio"
        )

    in_path, out_path, ratio_text = args
    ratio = float(ratio_text)
    if not (0.0 < ratio <= 1.0):
        raise SystemExit("ratio must be in (0.0, 1.0]")
    return in_path, out_path, ratio


def clear_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)


def import_glb(path: str) -> None:
    bpy.ops.import_scene.gltf(filepath=path)


def decimate_mesh_objects(ratio: float) -> None:
    for obj in bpy.data.objects:
        if obj.type != "MESH":
            continue

        # Keep at least a tiny reduction threshold to avoid no-op modifier work.
        if ratio >= 0.999:
            continue

        mod = obj.modifiers.new(name="LOD_Decimate", type="DECIMATE")
        mod.decimate_type = "COLLAPSE"
        mod.ratio = ratio
        mod.use_collapse_triangulate = True

        bpy.ops.object.select_all(action="DESELECT")
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.modifier_apply(modifier=mod.name)


def export_glb(path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)

    use_draco = os.getenv("BLENDER_DRACO", "1") == "1"
    position_q = int(os.getenv("BLENDER_DRACO_POSITION_Q", "10"))
    normal_q = int(os.getenv("BLENDER_DRACO_NORMAL_Q", "8"))
    texcoord_q = int(os.getenv("BLENDER_DRACO_TEXCOORD_Q", "8"))
    color_q = int(os.getenv("BLENDER_DRACO_COLOR_Q", "8"))

    kwargs = dict(
        filepath=path,
        export_format="GLB",
        export_yup=True,
        export_apply=False,
        export_texcoords=True,
        export_normals=True,
        export_materials="EXPORT",
        export_vertex_color="MATERIAL",
        export_cameras=False,
        export_lights=False,
    )

    if use_draco:
        kwargs["export_draco_mesh_compression_enable"] = True
        kwargs["export_draco_mesh_compression_level"] = 6
        kwargs["export_draco_position_quantization"] = position_q
        kwargs["export_draco_normal_quantization"] = normal_q
        kwargs["export_draco_texcoord_quantization"] = texcoord_q
        kwargs["export_draco_color_quantization"] = color_q

    bpy.ops.export_scene.gltf(**kwargs)


def main() -> None:
    in_path, out_path, ratio = parse_args()
    in_path = os.path.abspath(in_path)
    out_path = os.path.abspath(out_path)

    print(f"Input GLB: {in_path}")
    print(f"Output GLB: {out_path}")
    print(f"Decimate ratio: {ratio}")

    clear_scene()
    import_glb(in_path)
    decimate_mesh_objects(ratio)
    export_glb(out_path)
    print("Done")


if __name__ == "__main__":
    main()
