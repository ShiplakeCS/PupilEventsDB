class EventsDB:

    staff={}

    def __init__(self):
        file = open("PupilEvents2016-12-01.csv")
        file.readline()
        for line in file:
            line = line.rstrip("\n")
            collom = line.split(",")
            print(collom) # Don't need this once you know it's working

            if collom[1] in self.staff.keys():
                pass
            else:
                self.staff[collom[1]]=Teacher()

        print (self.staff.keys())  # Don't need this once you know it's working
        print(self.staff())  # Don't need this once you know it's working

    #TODO: add a 'getTeacher(staffcode)' method that will return the teacher object for the specific teacher
    #TODO: add a 'getStaffCodes()' method that will return a list of all the staff codes (keys) in the staff dictionary



class Teacher:
    __events=[]
    __numinf=0
    __numinc=0
    __numexc=0
    __subject=None
    def addevent(self, event):
        addevent(collom[0])
        if event == "EXC": # We're not testing if the event IS "EXC" but whether it CONTAINS "EXC", therefore use if "EXC" in event:
            __numexc=+ 1 # Needs to be self.__numexc in order to reference the class property
        elif event == "INF":
            __numinf=+ 1
        elif event== "INC":
            __numinc=+ 1




    def assignsubject(self, subject):
        self.__subject=subject


    def getnuminc(self):
        return self.__numinc

    def getnumexc(self):
        return self.__numexc

    def getnuminf(self):
        return self.__numinf

    def getsubject(self, Subject):
        return self.__subject

class Subject:
    __name= None
    def setname(self, name):
        self.__name = name
    def getname(self, name):
        return self.__name


"""

We can ignore the classes below for now

class Pupilevent:
    __event= None

class Exslip(Pupilevent):
    __event="exc"
class Inf(Pupilevent):
    __event="inf"

class Inc(Pupilevent):
    __event="inc"

"""

DB=EventsDB # You need to put brackets on the end of the class name when making a new object of the class - i.e. DB = EventsDB()

"""
Don't need these

T=Teacher()
T.addevent()
T.getnumexc()
T.getnuminc()
T.getnuminf()
"""

# Test your program is working
