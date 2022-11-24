import hou

#creating geo node

sel = hou.selectedNodes()

import hou

#creating geo node

sel = hou.selectedNodes()

root = sel[0].parent()

node = root.collapseIntoSubnet(sel, sel[0].name())



#parmtemplate group class
group = node.parmTemplateGroup()

#Create a folder "My Parms"
folder = hou.FolderParmTemplate("folder", "THREE POINT LIGHT CONTROL")
folderSettings = hou.FolderParmTemplate("folderSettings", "Settings")
#create a float slider
intensity = hou.FloatParmTemplate("intensity", "Intensity", 1, (1, 0, 0),0,10)
exposure = hou.FloatParmTemplate("exposure", "Exposure", 1, (0, 0, 0),0,10)
enable = hou.ToggleParmTemplate("enable", "Enable",1, help = "Enable all my lights")
radius = hou.FloatParmTemplate("radius", "Radius", 2, (1, 1, 0),0,10)
color = hou.FloatParmTemplate("color", "Color", 3, default_value=(1, 1, 1), look = hou.parmLook.ColorSquare, naming_scheme = hou.parmNamingScheme.RGBA)


#Add intensity to folder
folder.addParmTemplate(enable)
folderSettings.addParmTemplate(intensity)
folderSettings.addParmTemplate(exposure)
folderSettings.addParmTemplate(radius)
folderSettings.addParmTemplate(color)

folder.addParmTemplate(folderSettings)
#Add our folder into the parmTemplate of Geo
group.append(folder)

group.hideFolder("Transform", 1)
group.hideFolder("Subnet",1)

#Assigning the group template into the geo tabs

node.setParmTemplateGroup(group)

condition = (hou.parmCondType.HideWhen,'{ enable == 0}' )

folderSettings.setConditional(condition[0],condition[1])
node.replaceSpareParmTuple(folderSettings.name(), folderSettings)

###
for lgt in node.children():
    lgt.parm("light_intensity").setExpression('ch("../intensity")')
    lgt.parm("light_exposure").setExpression('ch("../exposure")')
    lgt.parm("light_enable").setExpression('ch("../enable")')

    lgt.parm("light_colorr").setExpression('ch("../colorr")')
    lgt.parm("light_colorg").setExpression('ch("../colorg")')
    lgt.parm("light_colorb").setExpression('ch("../colorb")')
    
    lgt.parm("areasize1").setExpression('ch("../radiusx")')
    lgt.parm("areasize2").setExpression('ch("../radiusy")')

