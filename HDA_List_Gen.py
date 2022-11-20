import os
import hou
dir = os.environ

HDAlist=[]
for x, y in dir.items():
    if x == "HOUDINI_USER_PREF_DIR":
        pref = os.walk(y)
        for curpath, directories, files in pref:
            if "otils" in curpath:
                for file in files:
                    if file in HDAlist:
                        pass
                    else:
                        HDAlist.append(file)
hdas = """
""".join(HDAlist)
hou.ui.displayMessage("Your HDAs are : " + """

""" + hdas)
