from ui.shared_path import Shared_Path
from ui.director_path import Director_Path
from ui.manager_path import Manager_Path
from logic.logic_wrapper import logic_wrapper


def main():
    user_input = Shared_Path.landing_page()
    if user_input == "m":
        Manager_Path.manager_menu()
    elif user_input == "d":
        director_input = Director_Path.director_menu()
        if director_input == "0":
            Shared_Path.voyage_list()
    print("help")
    print("Hello world")


if __name__ == "__main__":
    main()
