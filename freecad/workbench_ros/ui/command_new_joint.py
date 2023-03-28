import FreeCAD as fc

import FreeCADGui as fcgui

from ..gui_utils import tr
from ..utils import is_robot_selected


class _NewJointCommand:
    """The command definition to create a new Joint object."""

    def GetResources(self):
        return {'Pixmap': 'joint.svg',
                'Accel': 'N, J',
                'ToolTip': tr('Create a Joint.')}

    def IsActive(self):
        return is_robot_selected()

    def Activated(self):
        fc.activeDocument().openTransaction('Create Joint')
        fcgui.doCommand('')
        fcgui.addModule('freecad.workbench_ros.joint')
        fcgui.doCommand("_joint = freecad.workbench_ros.joint.make_joint('Joint')")
        fcgui.doCommand('FreeCADGui.ActiveDocument.setEdit(_joint.Name)')


fcgui.addCommand('NewJoint', _NewJointCommand())
