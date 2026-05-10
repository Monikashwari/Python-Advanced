from pathlib import Path


def file_converter(file_type): # This is the main function which will take the file type as an argument and return the decorator function which will add the functionality of converting the file to the original function.

    def decorator(fx): # This is the decorator function which will take the original function as an argument and return the main function which will add the functionality of converting the file to the original function.

        def main_fun(*args):
            print("Converting file...")

            response = fx(*args)

            input_file = args[0]
            base_name = Path(input_file).stem # This will give us the base name of the file without the extension. For example, if the input file is "orders.csv", the base name will be "orders".

            output_file = f"{base_name}.{file_type}"

            if file_type == "json":
                response.to_json(
                    output_file,
                    orient="records",
                    lines=True
                )

            elif file_type == "parquet":
                response.to_parquet(output_file)

            print(
                f"File converted successfully! "
                f"{output_file} is created."
            )

            return response

        return main_fun

    return decorator

@file_converter("parquet")
def csv_to_parquet(file_path:str):
    import pandas as pd
    df = pd.read_csv(file_path)
    return df

@file_converter ("json")
def csv_to_json(file_path:str):
    import pandas as pd
    df = pd.read_csv(file_path)
    return df

print(csv_to_json("orders.csv"))
print(csv_to_parquet("orders.csv"))
