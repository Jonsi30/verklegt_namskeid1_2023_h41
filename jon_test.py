
from data.destination_data import Destination_data
from model.destination import Destination
from model.voyage_model import Voyage_Model
from data.voyage_data import Voyage_Data


        # id,
        # flight_nr,
        # dep_from,
        # arr_at,
        # dep_time,
        # arr_time,
        # dep_time_back,
        # arr_time_back,
        # plane_insignia

id = input("Enter new voyage id: ")
flight_nr = input("Enter flight number: ")
dep_from = input("Enter departing airport: ")
arr_at = input("Enter arriving airport: ")
dep_time = input("Enter departure time: ")
arr_time = input("Enter time of arrival: ")
dep_time_back = input("Enter departure time back: ")
arr_time_back = input("Enter arrival time back: ")
plane_insignia = input("Enter plane_insignia: ")
captain="captain needed"
copilot="copilot needed"
head_of_service="head of service needed"
flight_attendant="flight attendant needed"

air = Voyage_Model(id, flight_nr, dep_from , arr_at, dep_time, arr_time, dep_time_back, arr_time_back, plane_insignia, captain, copilot, head_of_service, flight_attendant) 
Voyage_Data().create_voyage(air)