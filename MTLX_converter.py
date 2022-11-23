import hou

mysel = hou.selectedNodes()[0]

matcontext = mysel.parent()

#define output surface
matsubnet = matc ontext.createNode("subnet", mysel.name() + "_materialX")

surfaceoutput = matsubnet.createNode("subnetconnector", "surface_output")

#define output displacement
surfaceoutput.parm("parmname").set

#Create MTLX STD
