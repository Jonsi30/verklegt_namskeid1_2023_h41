from UI.landing_page import Landing_page
from UI.director_path import director_path
from UI.manager_path import manager_path


def main():
    user_input = Landing_page.landing_page()
    if user_input == "m":
        manager_path.manager_menu()
    elif user_input == "d":
        director_path.director_menu()
    print("help")
    print("Hello world")


if __name__ == "__main__":
    main()
