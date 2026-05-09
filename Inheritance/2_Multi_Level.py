class company : 
    def __init__(self,company_name:str):
        self.company_name:str = company_name
    
    def info(self):
        print(f"Company Name : {self.company_name}")
        return f"Company Name : {self.company_name}"

class manager(company):
    def __init__(self,company_name:str,manager_name:str):
        self.company_name = company_name
        self.manager_name = manager_name
    def manager_info(self):
        response = company.info(self)
        print(f"Manager Name : {self.manager_name},{response}")
        return f"Manager Name : {self.manager_name},{response}"

class employee(manager): 
    def __init__(self,employee_name:str,manager_name:str,company_name:str): # In child class connstructor we always need to declare and assign the parent class's attributes
        self.employee_name:str = employee_name
        self.manager_name:str = manager_name
        self.company_name:str = company_name

    def employee_info(self):
        response = manager.manager_info(self)
        print(f"Employee Name : {self.employee_name},{response}")

obj = employee("Marry Waston","John Smith","Google")
obj.employee_info() # Employee Name : Marry Waston,Manager Name : John Smith,Company Name : Google 