from os import system
from utils import *
from soldier_manager import *
from duty_manager import * 

def show_menu() -> None:
    print("""        === Duties managment ===     
          
    1.  Add soldier.
    2.  Remove soldier.
    3.  view soldiers.
    4.  Add duty.
    5.  Update duty status.
    6.  View soldier duties.
    7.  Exit.
    
    """)


def get_user_choice() -> str:
    return input("Choose an option: ")
    
def handle_add_soldier() -> None:
    id = int(input("Input soldier's ID: "))
    name = input("Input soldier's name: ")
    try:
        add_soldier(id, name)
    except ValueError:
        print("Invalid input")

def handle_remove_soldier() -> None:
    id = int(input("Input soldier's ID: "))
    try:
        remove_soldier(id)
    except KeyError:
        print("Soldier or duty not found")

def handle_view_soldiers() -> None:
    soldiers = get_all_soldiers()
    print(*soldiers, sep='\n')

def handle_add_duty() -> None:
    id = int(input("Enter soldier's ID: "))
    duty_name = input("Enter duty's name: ")
    day = input("Enter duty's day: ")
    try:
        add_duty_to_soldier(id, duty_name, day)
    except KeyError:
        print("Soldier or duty not found")
    except ValueError:
        print("Invalid input")

def handle_update_duty_status() -> None:
    id = int(input("Enter soldier's Id: "))
    duty = input("Enter duty's name: ")
    new_status = input("Enter the status you want change for(completed/missed): ")
    try:
        update_duty_status(id, duty, new_status)
    except KeyError:
        print("Soldier or duty not found")
    except ValueError:
        print("Invalid status")


def handle_view_soldier_duties() -> None:
    id = int(input("Enter soldier's ID: "))
    try:
        soldiers = get_soldier_duties(id)
        for soldier in soldiers:
            print(*soldier, sep='\n')
    except KeyError:
        print("Soldier not found")

def main() -> None:
    to_exit = False
    while not to_exit:
        show_menu()
        choice = get_user_choice()
        match choice:
            case '1':
                handle_add_soldier()
            case '2':
                handle_remove_soldier()
            case '3':
                handle_view_soldiers()
            case '4':
                handle_add_duty()
            case '5':
                handle_update_duty_status()
            case '6':
                handle_view_soldier_duties()
            case '7':
                to_exit = True
            case _:
                print("\nInvalid input.\nTry again.\n")
                input("Press Enter to continue...")
                system('clear')


if __name__ == '__main__':
    main()