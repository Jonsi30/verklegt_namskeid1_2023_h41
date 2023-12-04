from UI.Ui_main_menu import Main_menu

def main():
    user_input = Main_menu.landing_page()
    if user_input == "m":
        Main_menu.manager_menu()
    elif user_input == "d":
        Main_menu.director_menu()
    print("help")
    print("Hello world")

if __name__ == "__main__":
    main()
