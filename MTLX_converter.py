#MTLK Converter converts existing principled shaders into MaterialX networks which run faster and more efficiently particularly when using Solaris and Karma renderer.

#import mod
import hou

mysel = hou.selectedNodes()[0]

matcontext = mysel.parent()

#define output surface
matsubnet = matcontext.createNode("subnet", mysel.name() + "_materialX")

surfaceoutput = matsubnet.createNode("subnetconnector", "surface_output")
surfaceoutput.parm("parmname").set("surface")
surfaceoutput.parm("parmlabel").set("Surface")
surfaceoutput.parm("parmtype").set("surface")
surfaceoutput.parm("connectorkind").set("output") 

#define output displacement
dispoutput = matsubnet.createNode("subnetconnector", "surface_output")
dispoutput.parm("parmname").set("Displacement")
dispoutput.parm("parmlabel").set("Displacement")
dispoutput.parm("parmtype").set("displacement")
dispoutput.parm("connectorkind").set("output") 

#Create Albedo
path = mysel.parm("basecolor_texture").eval()
matsubnet.createNode("mtlximage", "Albedo")
albedo.parm("file").set(path)
mtlx.setInput(1, albedo)

#Create MTLX STD
mtlx = matsubnet.createNode("mtlxstandard_surface", "surface_mtlx")
surfaceoutput.setInput(0, mtlx)
matsubnet.layoutChildren()
