file= open("PupilEvents2016-12-01.csv", "r")

class Teacher:
    __events=[]
    __numinf=None
    __numinc=None
    __numexc=None
    __subject=None
    def addevent(self, events):
        self.__events.append(events)

    def assignsubject(self, subject):
        self.__subject=subject

    # def getnuminc(self, Inc):
    #     self.__numinc= Inc # 'get' methods do not need to accept parameters, and they do not assign new values to the class's properties. Instead, they simply return the value in the relevant property for the class. See corrected method code below and then make changes to your other get methods.

    def getnuminc(self):
        return self.__numinc

    def getnumexc(self, Exc):
        self.__numexc= Exc

    def getnuminf(self, Inf):
        self.__numinf= Inf

    def getsubject(self, Subject):
        self.__subject= Subject

class Subject:
    __name= None
    def setname(self, name):
        self #This needs completing
    def getname(self, name):
        self.__name= name

class Pupilevent:
    __event= None

class Exslip(Pupilevent):
    type="exc" # Check for consistency - in the parent class (Pupilevent) you have a property called __event whereas in these child classes you have the property called type. You should be using __event="exc" here and in the other child classes for Pupilevent

class Inf(Pupilevent):
    type="inf"

class Inc(Pupilevent):
    type="inc"

staff={}
staffcode=input("input staffcode\n") # Rather than have the user type in staff codes, this should be automatically loaded in from the CSV file that you have opened at the start of your program
#staff[staffcode]=Teacher(staffcode)
staff[staffcode]=Teacher() # No need to provide the staff code as an argument to the Teacher object's constructor method
