from datetime import datetime
def main():


    print("INPUT DATE (DD.MM.YYYY):")
        
    date_input = input("=> ")

    while validate_date_input(date_input) == False:
        print("Invalid date format, must be DD.MM.YYYY, try again!")
        date_input = input("=> ")
    
    print(date_input)


def validate_date_input(date_input) -> bool:
        """Input date must be in this format: DD.MM.YYYY"""
        try:
            if len(date_input) == 10:
                if date_input[2] == "." and date_input[5] == ".":
                    for letter in date_input:
                        if letter.isalpha():
                            return False
                        day = date_input[0]+date_input[1]
                        month = date_input[3]+date_input[4]
                        year = date_input[6:]
                        datetime(int(year), int(month), int(day))
                        
                        return True
                return False       
            return False
        except ValueError:
            """datetime function return ValueError if invalid date"""
            return False
                        
        
        
if __name__ == "__main__":
     main()