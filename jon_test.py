from data.voyage_data import GetData
from data.destination_data import Destination_data
from model.destination import Destination




dest = input("enter dest: ")
distance = input("Enter flight time: ")
flight_time = input("Enter flight time: ")
emergency_contact = input("Enter emergency contact: ")
emergency_contact_phone_nr = input("Emergency contact phone number: ")

air = Destination(dest, distance, flight_time, emergency_contact, emergency_contact_phone_nr)

Destination_data().update_destination(air)