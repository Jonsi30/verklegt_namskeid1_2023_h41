from UI.Ui_main_menu import Main_menu

def main():
    user_input = Main_menu.landing_page()
    if user_input == "m":
        user_input = Main_menu.manager_menu()
    elif user_input == "d":
        user_input = Main_menu.director_menu()

if __name__ == "__main__":
    main()
