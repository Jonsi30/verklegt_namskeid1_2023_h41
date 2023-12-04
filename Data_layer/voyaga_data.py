class GetData:
    def __init__(self) -> None:
        pass
    
    def get_voyage_data():
        try: 
            file_name = input(f"Enter voyage filename: ") #filenameið sem inniheldur info um þetta class
            file = open(file_name, "r")
            return file             
        except FileNotFoundError:
            print("File not found, try again")
