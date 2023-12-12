from data.voyage_data import Voyage_Data
from model.voyage_model import Voyage_Model


test = Voyage_Data()

new_voayge = test.create_voyage(Voyage_Model('1112', 'NA020', 'RVK', 'Nuuk', '06:00 16.12.2023', '09:00 16.12.2023', '12:00 16.12.2023', '15:00 16.12.2023', 'TF-20', 'Unassigned', 'Unassigned', 'Unassigned', 'Unassigned'))

