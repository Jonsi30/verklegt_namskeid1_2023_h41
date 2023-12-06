from ui.voyage_UI import voyage
from ui.main_UI import main_UI
from ui.Destination_UI import destination
from ui.Aircraft_UI import Aircraft

# from logic.logic_wrapper import Logic_wrapper


def main():
    m = main_UI()
    user_input = m.landing_page()
    if user_input == "m":
        main_UI.manager_menu()
    elif user_input == "d":
        director_input = main_UI.director_menu()
        if director_input == "0":
            all_voyages = voyage().format_voyages()
            print(all_voyages)
        if director_input == "2":
            Aircraft().get_all_aircrafts()
            director_input = Aircraft().get_all_aircrafts()
            if director_input == "n":
                Aircraft().create_new_aircraft()
        if director_input == "3":
            destination().get_all_destinations()
            director_input = destination().get_all_destinations()
            if director_input == "n":
                destination().create_new_destination()


if __name__ == "__main__":
    main()
