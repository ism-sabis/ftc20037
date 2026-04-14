#!/usr/bin/env python3
"""Convert OBJ+MTL to GLB using Blender in headless mode.

Usage:
  blender -b -P scripts/blender_obj_to_glb.py -- input.obj output.glb
"""

import os
import sys

import bpy


def parse_args() -> tuple[str, str]:
    if "--" not in sys.argv:
        raise SystemExit("Missing '--' before input/output arguments")
    args = sys.argv[sys.argv.index("--") + 1 :]
    if len(args) != 2:
        raise SystemExit("Usage: blender -b -P blender_obj_to_glb.py -- input.obj output.glb")
    return args[0], args[1]


def clear_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)


def import_obj(path: str) -> None:
    if hasattr(bpy.ops.wm, "obj_import"):
        bpy.ops.wm.obj_import(filepath=path, forward_axis="NEGATIVE_Z", up_axis="Y")
    else:
        bpy.ops.import_scene.obj(filepath=path, axis_forward="-Z", axis_up="Y")


def export_glb(path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    use_gltfpack = os.getenv("BLENDER_GLTFPACK", "0") == "1"
    use_draco = os.getenv("BLENDER_DRACO", "0") == "1"
    gltfpack_si = float(os.getenv("BLENDER_GLTFPACK_SI", "1.0"))

    export_kwargs = dict(
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

    if use_gltfpack:
        export_kwargs["export_use_gltfpack"] = True
        export_kwargs["export_gltfpack_si"] = gltfpack_si

    if use_draco:
        position_q = int(os.getenv("BLENDER_DRACO_POSITION_Q", "14"))
        normal_q = int(os.getenv("BLENDER_DRACO_NORMAL_Q", "10"))
        texcoord_q = int(os.getenv("BLENDER_DRACO_TEXCOORD_Q", "12"))
        color_q = int(os.getenv("BLENDER_DRACO_COLOR_Q", "10"))
        export_kwargs["export_draco_mesh_compression_enable"] = True
        export_kwargs["export_draco_mesh_compression_level"] = 6
        export_kwargs["export_draco_position_quantization"] = position_q
        export_kwargs["export_draco_normal_quantization"] = normal_q
        export_kwargs["export_draco_texcoord_quantization"] = texcoord_q
        export_kwargs["export_draco_color_quantization"] = color_q

    bpy.ops.export_scene.gltf(**export_kwargs)


def main() -> None:
    in_path, out_path = parse_args()
    in_path = os.path.abspath(in_path)
    out_path = os.path.abspath(out_path)

    print(f"Input OBJ: {in_path}")
    print(f"Output GLB: {out_path}")

    clear_scene()
    import_obj(in_path)
    export_glb(out_path)
    print("Done")


if __name__ == "__main__":
    main()