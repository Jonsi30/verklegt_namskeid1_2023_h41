
from data.data_wrapper import Data_wrapper
def main():
    
    name = Data_wrapper()
    
    id = str(input("Enter new id: "))
    id = id.upper()
    destination = input("Enter new destination: ")
    numeric_id = input("Enter numeric id: ")

    name.create_destination(id, destination, numeric_id)
    all_destinations = name.get_all_destinations()
    
    for destination in all_destinations:
        
        print(destination)

    


if __name__ == "__main__":
    main()