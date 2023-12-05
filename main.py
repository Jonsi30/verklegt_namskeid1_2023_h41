from ui.shared_path import Shared_path
from ui.director_path import director_path
from ui.manager_path import manager_path
from logic.logic_wrapper import logic_wrapper


def main():
    user_input = Shared_path.landing_page()
    if user_input == "m":
        manager_path.manager_menu()
    elif user_input == "d":
        director_input = director_path.director_menu()
        if director_input == "0":
            Shared_path.voyage_list()
    print("help")
    print("Hello world")


if __name__ == "__main__":
    main()
