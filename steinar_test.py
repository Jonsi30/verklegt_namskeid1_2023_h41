from data.destination_data import Destination_data
from model.destination import Destination

def main():
    
    name = Destination_data()
    """
    id = str(input("Enter new id: "))
    id = id.upper()
    destination = input("Enter new destination: ")
    numeric_id = input("Enter numeric id: ")

    info = f'"{id}", "{destination}", "{numeric_id}"'

    new_destination = Destination(f'{id}', f'{destination}', f'{numeric_id}')
    name.create_destination(new_destination)"""
    all_destinations = name.get_all_destination()
    
    for destination in all_destinations:
        
        print(destination)

    


if __name__ == "__main__":
    main()