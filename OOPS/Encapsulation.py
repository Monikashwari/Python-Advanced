class Myclass:
    #Class variables  
    var1 = "Monikashwari"
    var2 = "Saravanan"

    #Instance Variables
    def __init__(self,dyn1,dyn2,dyn3): #We use Access Modifiers for the security of the Variables (Public, Private, Protected)
        self.dyn1 = dyn1 #Public Variable
        self.__dyn2 = dyn2 #Private Variable (it is not accessible outside the class)
        self._dyn3 = dyn3 #Protected Variable (it is accessible outside the class but it is not recommended to access it outside the class)

    def func1(self):
        print(f"Hello World, {self.dyn1}")

    def func2(self):
        print(f"Hello Globe, {self.__dyn2}")

    def func3(self):
        print(f"Hello Globe, {self._dyn3}")


obj = Myclass("Data","Data Engineer","Devops")
obj.func1()
obj.func2()
obj.func3()
print(obj.dyn1) 
obj.dyn1 = "abc" 
print(f"After modification: {obj.dyn1}")

obj.dyn2 = "xyz" # It will create a new variable dyn2 in the object and it will not modify the private variable __dyn2
print(obj.dyn2) # It will print the new variable dyn2

print(obj._dyn3) 
obj._dyn3 = "pqr" # It will modify the protected variable _dyn3 but it is not recommended to modify it outside the class
print(f"After modification: {obj._dyn3}")

print(obj.__dyn2) # It will give an error because __dyn2 is a private variable and it is not accessible outside the class
obj.__dyn2 = "xyz"
    