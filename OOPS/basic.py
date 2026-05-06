class Myclass:

    #Class variables or Attributes (creating while class creation which are common for all the objects created from the class)
    var1 = "Monikashwari"
    var2 = "Saravanan"

    #Functions or Methods
    def func1(self):
        print("Hello Data World...")
    def func2(self):
        print("I'm a Data Engineer!!")
    
#Creating Object (For accessing the Class multiple times wherever we want to use it)    
obj = Myclass()
obj1 = Myclass()
obj.func1()
obj1.func2()
