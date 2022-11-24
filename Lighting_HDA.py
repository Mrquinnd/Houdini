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
folder = hou.FolderParmTemplate("folder", "My Parms")
folderSettings = hou.FolderParmTemplate("folderSettings", "Settings")
#create a float slider
intensity = hou.FloatParmTemplate("intensity", "Intensity", 1, (1, 0, 0),0,10)
exposure = hou.FloatParmTemplate("exposure", "Exposure", 1, (0, 0, 0),0,10)
enable = hou.ToggleParmTemplate("enable", "Enable",1, help = "Enable all my lights")
radius = hou.FloatParmTemplate("radius", "Radius", 2, (1, 1, 0),0,10)


#Add intensity to folder
folder.addParmTemplate(enable)
folderSettings.addParmTemplate(intensity)
folderSettings.addParmTemplate(exposure)

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
