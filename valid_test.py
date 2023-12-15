def main():


    Contact = """
        
    Emergency contact name"""
    print(Contact)
    contact_input = input("=> ")

    while validate_emergency_contact_name(contact_input) == False:
        print("Invalid emergency contact name!")
        contact_input = input("=> ")
    
    print(contact_input)


def validate_emergency_contact_name(contact_input) -> bool:
        """Duration must be in a correct from"""
        
        if len(contact_input) > 5:
            
                        return True
                    
        return False
        
        
if __name__ == "__main__":
     main()