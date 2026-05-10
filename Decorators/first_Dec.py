"""Decorators are a powerful tool in Python that allows you to modify the behavior of a function or class. 
A decorator is a function that takes another function as an argument and  exends its behavior without explicitly modifying it. 
Decorators are often used to add functionality to existing code, such as logging, timing, or access control. 
In this example, we will create a simple decorator that prints a message before and after calling the original function.
"""
def first_decorator(fx):
    def main_fun(*args): #this is the main function which will be returned by the decorator function. This function will take any number of arguments and pass it to the original function.
        print("Before calling the function")
        response = fx(*args) # Here we are calling the original function and passing the arguments to it. The response from the original function is stored in the response variable. We can modify this response if we want to add some functionality to it.
        print("After calling the function")
        return response
    return main_fun

@first_decorator # This will add the functionality of the first_decorator to the fetch_data function. This is equivalent to writing fetch_data = first_decorator(fetch_data)
def fetch_data(url:str,path:str):
    return f"fetching data from {url} and saved in {path}"

print(fetch_data("https://api.example.com/data","/data/data.json"))