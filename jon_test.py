from data.voyage_data import GetData
from data.destination_data import Destination_data
from model.destination import Destination

air = Destination('Nuuk', '1234', '4:30', 'Helgo', '555555555')
Destination_data().update_destination(air)