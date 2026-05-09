class company : 
    def __init__(self,company_name:str):
        self.company_name:str = company_name
    
    def info(self):
        print(f"Company Name : {self.company_name}")
        return f"Company Name : {self.company_name}"

class employee(company): # employee class is child class of company class
    def __init__(self,employee_name:str,company_name:str): # In child class connstructor we always need to declare and assign the parent class's attributes
        self.employee_name:str = employee_name
        self.company_name:str = company_name

    def employee_info(self):
        response = company.info(self) #
        print(f"Employee Name : {self.employee_name},{response}")

obj = employee("James","Amazon")
obj.employee_info() # Employee Name : James,Company Name : Amazon
