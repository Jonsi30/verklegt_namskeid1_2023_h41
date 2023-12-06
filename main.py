from ui.main_UI import main_UI

from logic.logic_wrapper import logic_wrapper


def main():
    m = main_UI()
    user_input = m.landing_page()
    if user_input == "m":
        main_UI.manager_menu()
    elif user_input == "d":
        director_input = main_UI.director_menu()
        if director_input == "0":
            all_voyages = logic_wrapper().get_all_voyages()
            for voyage in all_voyages:
                print(voyage)


if __name__ == "__main__":
    main()
