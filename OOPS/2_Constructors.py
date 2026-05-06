class Myclass:

    #Class variables or Attributes (creating while class creation which are common for all the objects created from the class)
    var1 = "Monikashwari"
    var2 = "Saravanan"

     # Instance Variables or Dynamic Variables (creating while object creation which are different for all the objects created from the class)
     #this function is triggered automatically when we create an object from the class and it is used to initialize the instance variables
    
    def __init__(self,dyn1,dyn2,dyn3): #Constructor (a special function which is used to create the instance variables)
        self.dyn1 = dyn1 # self is a keyword which is used to refer to the current object (it is used to access the instance variables)
        self.dyn2 = dyn2
        self.dyn3 = dyn3

    def func1(self):
        print(f"Hello World, {self.dyn1}")

    def func2(self):
        print(f"Hello Globe, {self.dyn2}")

    def func3(self):
        print(f"Hello Globe, {self.dyn3}")


obj = Myclass("Data","Data Engineer","Devops")
obj.func1()
obj.func2()
obj.func3()

# Another Way to call the function
Myclass.func2(obj)
    