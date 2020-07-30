# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

#
# 为‘工设狗的blender之路‘教程开发的便利插件
#

bl_info = {
    "name": "Add View Camera ",
    "author": "Atticus",
    "version": (0, 0, 1),
    "blender": (2, 83, 2),
    "location": "View3D > Add > Camera > Add View Cam",
    "description": "Add View Cam",
    "doc_url": "",
    "tracker_url": "",
    "category": "Camera",
}

import bpy

def add_cam_menu(self, context):
    # add menu
    if context.mode == 'OBJECT':
        self.layout.operator("object.addviewcam",icon='VIEW_CAMERA')


class AddViewCam(bpy.types.Operator):
    """add view cam"""
    bl_idname = "object.addviewcam"
    bl_label = "Add View Cam"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        #Add cam
        bpy.ops.object.camera_add()
        camName = context.object.name;cam = bpy.data.objects[camName]
        bpy.context.scene.camera = cam

        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        area.spaces[0].region_3d.view_perspective = 'PERSP'
                        override = {'area': area, 'region': region}
                        bpy.ops.view3d.camera_to_view(override)
                break

        return {'FINISHED'}

classes = (AddViewCam,)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    bpy.types.VIEW3D_MT_camera_add.append(add_cam_menu)


def unregister():
    from bpy.utils import unregister_class
    for cls in classes:
        unregister_class(cls)

    bpy.types.VIEW3D_MT_camera_add.remove(add_cam_menu)

if __name__ == '__main__':
    register()