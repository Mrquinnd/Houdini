import hou
import os

textureChannels = ['BaseColor', 'Roughness', 'Height', 'Opacity', 'Metalness']

selected_nodes = hou.selectedNodes()

if not selected_nodes:
    raise Exception("Please select a Material Library node.")
else:
    print("Selected nodes:", selected_nodes)

material_library_node = selected_nodes[0]
print("Selected Material Library node:", material_library_node)

if material_library_node.type().name() != "materiallibrary":
    raise Exception("Selected node is not a Material Library node.")
else:
    print("The selected node is a Material Library node.")

    selection = hou.selectedNodes()[0]
    
    context = selection.parent()
    
    materialx = selection.createNode("mtlxstandard_surface", "_mtlx")
    texture_node = material_library_node.createNode("usduvtexture", "Diffuse")
 

# Layout the new nodes
material_library_node.layoutChildren()

print("Node creation and layout complete.")
    
selection.layoutChildren()
