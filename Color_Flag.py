#Apply a specific style to the type of Node.

import hou

obj = hou.node("/obj")

mysel = hou.selectedNodes()

for node in mysel:
    flag = node.isDisplayFlagSet()
    if flag == 1:
        node.setColor(hou.Color(0,1,0))
    if flag == 0:
        node.setColor(hou.Color(1,0,0))
        print(node.name() + " my display is OFF")
