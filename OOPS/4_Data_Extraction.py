import pandas as pd
class Data_Extraction:
   def __init__(self,file_path:str):
      self.file_path = file_path
    
   def extract_data(self,seperator:str):
       df = pd.read_csv(self.file_path,sep=seperator)
       print(df.head())   
   def extract_json(self):
       df = pd.read_json(self.file_path)
       print(df.head())
   def extract_parquet(self): #pre-requisite: pip install pyarrow or pip install fastparquet(lightweight)--> for parquet file handling
       df = pd.read_parquet(self.file_path)
       pd.set_option('display.max_columns', None)# to display all the columns in the dataframe (Because pandas defaultly truncates the columns)
       print(df.head())
      
while choice := input("Do you want to extract data? (yes/no): ").lower() == "yes":
    print("Select the file format to extract data:")
    print("1. CSV")
    print("2. TSV")
    print("3. JSON")
    print("4. Parquet")
    choice = input("Enter your choice: ")

    if choice == "1":
        obj = Data_Extraction("Files/orders.csv")
        obj.extract_data(",")
    elif choice == "2":
        obj = Data_Extraction("Files/orders.tsv")
        obj.extract_data("\t")
    elif choice == "3":
        obj = Data_Extraction("Files/orders.json")
        obj.extract_json()
    elif choice == "4":
        obj = Data_Extraction("Files/orders.parquet")
        obj.extract_parquet()
    else:
        print("Invalid choice!")
