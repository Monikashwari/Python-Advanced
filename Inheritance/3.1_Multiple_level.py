# This is an examle of Multiple level inheritance . In this example one parent cless is inherited by two child classes. 
class company : 
    def __init__(self,company_name:str):
        self.company_name:str = company_name
    
    def info(self):
        print(f"Company Name : {self.company_name}")
        return f"Company Name : {self.company_name}"

class employee(company):
    def __init__(self,company_name:str,employee_name:str):
        self.company_name = company_name
        self.employee_name = employee_name
    def employee_info(self):
        response = company.info(self)
        print(f"Employee Name : {self.employee_name},{response}")
        
class contractor(company): 
    def __init__(self,company_name,contractor_name): 
        self.company_name = company_name
        self.contractor_name = contractor_name
    def contractor_info(self):
        response = company.info(self) # Here we are calling the parent class's method using the child class's object. We can also call the parent class's method using the parent class's name and passing the child class's object as an argument.
        print(f"Contractor Name : {self.contractor_name},{response}")

obj1 = employee("Paypal","Marry")
obj1.employee_info() # Employee Name : Marry,Company Name : Paypal
obj2 = contractor("Paypal","Andreson")
obj2.contractor_info()# Contractor Name : Andreson,Company Name : Paypal