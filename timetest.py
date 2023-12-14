from logic.logic_wrapper import Logic_wrapper


voyage_id_list = []
Destination_id_list = []
destinations = []

for voyage in Logic_wrapper().get_all_voyages():
    voyage_id_list.append(voyage.id)

for destination in Logic_wrapper().get_all_destinations():
    Destination_id_list.append(destination.destination_id)
    destinations.append(destination)


id = f"""
Input a new ID(fx. 1111)
Id's that are unavailable are as follows: {", ".join(voyage_id_list)}"""
print(id)
id_input = input("=>: ")
if id_input in voyage_id_list:
    while id_input in voyage_id_list:
        print("ID has already been created! Please try again.")
        id_input = input("=>: ")


dep_from = f"""
Input the destination ID For the place you are Departuring from(fx. RVK)
Destination ID's we fly too are: {", ".join(Destination_id_list)}"""
print(dep_from)
dep_from_input = input("=>: ")
if dep_from_input not in Destination_id_list:
    while dep_from_input not in Destination_id_list:
        print("\n\tWe dont fly from any destination with that destination ID! Please try again.")
        dep_from_input = input("=>: ")

arr_at = """
Input destination ID for the place you are arriving at(fx. TOR)"""
print(arr_at)
arr_at_input = input("=>: ")
if arr_at_input not in Destination_id_list:
    while arr_at_input not in Destination_id_list:
        print("\n\tWe dont fly to any destination with that destination ID! Please try again.")
        arr_at_input = input("=>: ")

destination_flight_time = ""

for dest in destinations:
    if arr_at_input == dest.destination_id:
        destination_flight_time += (dest.flight_time)



print(destination_flight_time)


dep_time = '00:00 16.12.2023'

