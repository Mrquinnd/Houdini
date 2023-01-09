import hou

# create geo node
node = hou.node("/obj").createNode('subnet')

# parm template group class
group = node.parmTemplateGroup()

# create a folder called my parms

folder = hou.FolderParmTemplate("folder", "myParms")
folderSettings = hou.FolderParmTemplate("folderSettings", "Settings")
# create a float slider

intensity = hou.FloatParmTemplate("intensity", 'intensity', 2, (1,10,0), 0, 10)

enable = hou.ToggleParmTemplate("enable", "Enable", help = "Help enable all my lights.")

# add intensity to the folder
folder.addParmTemplate(folderSettings)

folderSettings.addParmTemplate(enable)
folderSettings.addParmTemplate(intensity)



# add our folder into parm template "geo1"

group.append(folder)
group.hideFolder("Transform", 1)
group.hideFolder("Subnet", 1)

#node.setParmTemplate(Group)

node.setParmTemplateGroup(group)

intensity.setConditional(hou.parmCondType.HideWhen,'{ enable == 1}')

condition = (hou.parmCondType.HideWhen, '{ enable == 0}')
folderSettings.setConditional = (condition[0], condition[1])

node.replaceSpareParmTuple(folderSettings.name(), folderSettings)


# Assigning the group conditional into the geo tabs


