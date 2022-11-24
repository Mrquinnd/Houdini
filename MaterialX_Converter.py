##MTLK Converter converts existing principled shaders into MaterialX networks which run faster and more efficiently particularly when using Solaris and Karma renderer.

##import mod
import hou

mysel = hou.selectedNodes()[0]

matcontext = mysel.parent()

##define output surface
matsubnet = matcontext.createNode("subnet", mysel.name() + "_materialX")

surfaceoutput = matsubnet.createNode("subnetconnector", "surface_output")
surfaceoutput.parm("parmname").set("surface")
surfaceoutput.parm("parmlabel").set("Surface")
surfaceoutput.parm("parmtype").set("surface")
surfaceoutput.parm("connectorkind").set("output") 

##define output displacement
dispoutput = matsubnet.createNode("subnetconnector", "surface_output")
dispoutput.parm("parmname").set("Displacement")
dispoutput.parm("parmlabel").set("Displacement")
dispoutput.parm("parmtype").set("displacement")
dispoutput.parm("connectorkind").set("output") 

##Create MTLX STD
mtlx = matsubnet.createNode("mtlxstandard_surface", "surface_mtlx")
surfaceoutput.setInput(0, mtlx)

##Create Albedo
path = mysel.parm("basecolor_texture").eval()
albedo = matsubnet.createNode("mtlximage", "Albedo")
albedo.parm("file").set(path)
mtlx.setInput(1, albedo)

##Create Roughness
path = mysel.parm("rough_texture").eval()
rough = matsubnet.createNode("mtlximage", "Roughness")
rough.parm("file").set(path)
#Specifying the colour value
rough.parm("signature").set("0")
mtlx.setInput(6, rough)

##Create Specular
if mysel.parm("reflect_useTexture").eval() == 1:
    path = mysel.parm("reflect_useTexture").eval()
    spec = matsubnet.createNode("mtlximage", "Reflect")
    spec.parm("file").set(path)
    mtlx.setInput(5, spec)
    
    

##Create Opacity
#Check the state
if mysel.parm("opaccolor_useTexture").eval() == 1:
    
    path = mysel.parm("opaccolor_useTexture").eval()
    opac = matsubnet.createNode("mtlximage", "Opacity")
    opac.parm("file").set(path)
    mtlx.setInput(38, opac)
    
##Create Normal
if mysel.parm("baseBumpAndNormal_enable").eval() == 1:
    path = mysel.parm("baseNormal_texture").eval()
    normal = matsubnet.createNode("mtlximage", "Normal")
    plugnormal = matsubnet.createNode("mtlxnormalmap")
    normal.parm("file").set(path)
    mtlx.setInput(40, plugnormal)
    plugnormal.setInput(0, normal)
    
   
##Create displacement
#If displacement texture is true.
if mysel.parm("dispTex_enable").eval() == 1:
    # Getting parm value
    path = mysel.parm("dispTex_texture").eval()
    offset = mysel.parm("dispTex_offset").eval()
    scale = mysel.parm("dispTex_scale").eval()
    
    # Getting displace nodes
    displace = matsubnet.createNode("mtlximage", "Displace")
    plugdisplace = matsubnet.createNode("mtlxdisplacement")
    remapdisplace = matsubnet.createNode("mtlxremap", 'Offset_Displace')
    
    #Setting parameter displace
    remapdisplace.parm("outlow").set(offset)
    plugdisplace.parm("scale").set(scale)
    displace.parm("file").set(path)
    displace.parm("signature").set("0")
    
    #Setting inputs
    dispoutput.setInput(0, plugdisplace)
    plugdisplace.setInput(0, displace)
    remapdisplace.setInput(0, displace)
    

 
#Organises nodes nicely
matsubnet.layoutChildren()

