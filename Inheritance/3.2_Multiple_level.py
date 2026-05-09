# Expample of Multiple level inheritance in Python. This example is about a child class inheriting from two parent classes. Here we have a company class and a client_company class. The employee class is inheriting from both the company and client_company classes. 
class company : 
    def __init__(self,company_name:str):
        self.company_name:str = company_name
    
    def info(self):
        print(f"Company Name : {self.company_name}")
        return f"Company Name : {self.company_name}"
class client_company :
    def __init__(self,client_company_name:str):
        self.client_company_name = client_company_name
    
    def info(self):
        print(f"Client Company Name : {self.client_company_name}")
        return f"Client Company Name : {self.client_company_name}"

class employee(company,client_company): 
    def __init__(self,company_name:str,client_company_name:str,employee_name:str):
        self.company_name = company_name
        self.client_company_name = client_company_name
        self.employee_name = employee_name
    def employee_info(self):
        response1 = company.info(self)
        response2 = client_company.info(self)
        print(f"Employee Name : {self.employee_name},{response1},{response2}")

obj = employee("Ford","Paytm","Kitty Covey")
obj.employee_info() # Employee Name : Kitty Covey,Company Name : Ford,Client Company Name : Paytm