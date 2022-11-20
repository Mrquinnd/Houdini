#Usng person variable. We use it to initialise a variable in the greeting class called name. We add a name argument in the init function. Once defined, the current iteration of this greeting loop should have a name property equal to its name.
import hou

class greetings():

    def __init__(self, name):
        self.name = name
        
        
    def hello(person):
        print("hello " + person.name)
    def bye(person):
        print("bye " + person.name)

personlist=["adrien", "edee", "john", "chris"]
for person in personlist:
    if person == "adrien":
        greetings(person).bye()
    else:
        greetings(person).hello()
