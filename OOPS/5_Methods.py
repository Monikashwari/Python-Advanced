"""There are three types of methods in python:
1. Instance method: It is the default method in python. It takes self as the first parameter. It cannot change the class variable for all the instances of the class. It can access and modify instance variables.
2. Class method: It takes cls as the first parameter and is defined using the @classmethod decorator. It can access and modify class variables for all the instances of the class.
3. Static method: It does not take self or cls as the first parameter and is defined using the @staticmethod decorator. It cannot access or modify class variables and is used for utility functions. It is not bound to any instance or class and can be called using the class name or instance name.
it is independent of the class and can be called without creating an instance of the class. It is used for utility functions that do not require access to class or instance variables."""

class type_methods:
    var_1 = 10

    def __init__(self):
        print("This is the constructor method")
    def __str__(self):
        print("This is the string method")

    @classmethod #decorator to define a class method
    def _change_value(cls,new_val):
        cls.var_1 = new_val
        print(f"Value of var_1 is changed to {cls.var_1}")
    
    @staticmethod #decorator to define a static method
    def dummy():
        print("This is a static method")
obj = type_methods()
print(obj.var_1) #10
obj.var_1 = 15 #This will create an instance variable var_1 for obj and will not change the class variable var_1
print(obj.var_1) #15
obj2 = type_methods()
print(obj2.var_1) #10
print("Using class method ...")
type_methods._change_value(20) #Value of var_1 is changed to 20
print(obj2.var_1) #20
type_methods.dummy() #This is a static method using class name
obj.dummy() #This is a static method using instance name
