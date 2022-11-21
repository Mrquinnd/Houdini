#import houdini modules
import hou

#Defines chosen context.
obj = hou.node("/obj")

#Initialise Blue variable
blue = 0

#Select colour panel.
colorui = hou.ui.selectColor()
print(colorui)

#For anything in range from 0 - 12.
for x in range(0,12):
    #Create a geo, create a sphere inside.
    geosphere = obj.createNode("geo", "geo_sphere" + str(x+1))
    sphere = geosphere.createNode("sphere")
    
#offsets position
    mypos = (x*3, 2+x)
    geosphere.setPosition(mypos)
    
    #colour defined in cl variable.
    cl = (0.2,5, blue)
    geosphere.setColor(hou.Color(cl))
    #incrementing variable blue on loop.
    blue += 0.1
