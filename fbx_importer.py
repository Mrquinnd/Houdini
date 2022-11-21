#houdini module
import hou

class assetimporter():
    def importobj(self):
        #Select objects
        mydir = hou.ui.selectFile(title="Choose your assets", multiple_select=1)
        mydir = mydir.split(" ;")
        
        #obj context
        obj = hou.node("obj")
        
        #create geo
        mygeo = obj.createNode("geo", "myassets")
        
        merge = mygeo.createNode("merge", "merge_asset")
        switch = mygeo.createNode("switch", "switch_asset")
        
        count =0
        for asset in mydir:
        
            #create/name file
            name = asset.split("/")
            name = (name[-1].split(".")[0])
            file = mygeo.createNode("file", name)
            
            #create the nodes
            material = mygeo.createNode("material", "material_" + name)
            pack = mygeo.createNode("pack", "pack_" + name)
            
            #Connect nodes
            material.setInput(0, file)
            pack.setInput(0, material)
            
            #set nodes
            pack.parm('pivot').set("origin")
            
            #file.parm("file").set(asset)
            
            merge.setInput(count, pack)
            switch.setInput(count, pack)
            count +=1
            
        mygeo.layoutChildren()
assetimporter().importobj()
