from ui.main_UI import main_UI
from ui.Destination_UI import destination
from logic.logic_wrapper import Logic_wrapper
from ui. import voyage


def main():
    m = main_UI()
    user_input = m.landing_page()
    if user_input == "m":
        main_UI.manager_menu()
    elif user_input == "d":
        director_input = main_UI.director_menu()
        if director_input == "0":
            pass
            # all_voyages = Logic_wrapper().get_all_voyages()
            # for voyage in all_voyages:
            #   print(voyage)
        if director_input == "3":
            destination().get_all_destinations()
            director_input = destination().get_all_destinations()
            if director_input == "n":
                destination().create_new_destination()


if __name__ == "__main__":
    main()
