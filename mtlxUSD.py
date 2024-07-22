import hou
import os

#Channels for substance painter
textureChannels = ['BaseColor', 'Roughness', 'Height', 'Opacity', 'Metalness']

#set the base name with prompt ("ex: watch_v2_wood")
baseName = hou.ui.readInput( initial_contents="mymaterial_wood" , message="Set the base object name", buttons= ["Save","Cancel"], title="Object BaseName")
#print(baseName)

if baseName[0]==0 and baseName[1] != '' :

    #set the textures directory with file input
    currentproject = os.path.dirname(hou.hipFile.path())
    
    pathToTextures = hou.ui.selectFile( file_type=hou.fileType.Directory, start_directory = currentproject, title = "Select the texture folder")
    
    selection = hou.selectedNodes()[0]
    
    context = selection.parent()
    
    materialx = selection.createNode("mtlxstandard_surface", baseName[1]+"_mtlx")
    
    UVNode = selection.createNode("mtlxtexcoord","UVS")
    UVNode.parm("signature").set("vector2")
