""" You just need to change the object to fetch data from different sources.
 This is the power of polymorphism. 
 We can use the same method name to fetch data from different sources. 
 This is also known as method overriding.
"""
class fetch_api:
    def fetch(self):
        print("Fetching data from API...")
        return "Data from API"
class fetch_database:
    def fetch(self):
        print("Fetching data from Database...")
        return "Data from Database"
class fetch_s3:
    def fetch(self):
        print("Fetching data from S3...")
        return "Data from S3"

obj = fetch_api() 
print(obj.fetch()) # Fetching data from API... Data from API
obj = fetch_database()
print(obj.fetch()) # Fetching data from Database... Data from Database
obj = fetch_s3()
print(obj.fetch()) # Fetching data from S3... Data from S3