def main():


    Number = """
        
    emergency contact phone_nr"""
    print(Number)
    contact_nr_input = input("=> ")

    while validate_emergency_contact_phone_nr(contact_nr_input) == False:
        print("Invalid emergency contact phone number!")
        contact_nr_input = input("=> ")
    
    print(contact_nr_input)


def validate_emergency_contact_name(contact_nr_input) -> bool:
        """Emergency contact phone number can't include letters"""
        
        if len(contact_nr_input) == 7:
            for number in contact_nr_input:
                 if number.isalpha():
                    return False
            return True       
        return False
        
        
if __name__ == "__main__":
     main()