from model.destination import Destination
from data.data_wrapper import Data_wrapper
def main():
    
    name = Data_wrapper()
    
    id = str(input("Enter new id: "))
    id = id.upper()
    destination = input("Enter new destination: ")
    numeric_id = input("Enter numeric id: ")

    info = f'"{id}", "{destination}", "{numeric_id}"'

    new_destination = (f'{id}', f'{destination}', f'{numeric_id}')
    name.create_destination(new_destination)
    all_destinations = name.get_all_destinations()
    
    for destination in all_destinations:
        
        print(destination)

    


if __name__ == "__main__":
    main()