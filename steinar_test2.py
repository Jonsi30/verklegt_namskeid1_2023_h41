from data.voyage_data import Voyage_Data

test = Voyage_Data()
listi = (test.get_all_voyage())

for item in listi:
    date = (item["arr_time_back"])
    print(date[6::])
    