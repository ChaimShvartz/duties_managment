# Link to GitHub - https://github.com/ChaimShvartz/duties_managment

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
    try:
        soldier_id = int(input("Input soldier's ID: "))
        name = input("Input soldier's name: ")
        add_soldier(soldier_id, name)
        print(f"V - {name.title()} added.")
    except ValueError as e:
        print('X -', e)

def handle_remove_soldier() -> None:
    try:
        soldier_id = int(input("Input soldier's ID: "))
        remove_soldier(soldier_id)
        print("V - the soldier removed.")
    except (KeyError, ValueError) as e:
        print('X -', e)

def handle_view_soldiers() -> None:
    soldiers = get_all_soldiers()
    if soldiers:
        print(', '.join(soldier["name"] for soldier in soldiers))
    else:
        print("There are not soldiers yet.")

def handle_add_duty() -> None:
    try:
        soldier_id = int(input("Enter soldier's ID: "))
        duty_name = input("Enter duty's name: ")
        day = input("Enter duty's day: ")
        add_duty_to_soldier(soldier_id, duty_name, day)
        print(f"V - {duty_name} adds.")
    except (KeyError, ValueError) as e:
        print('X -', e)

def handle_update_duty_status() -> None:
    try:
        soldier_id = int(input("Enter soldier's Id: "))
        duty = input("Enter duty's name: ")
        new_status = input("Enter the status you want change for(completed/missed): ")
        update_duty_status(soldier_id, duty, new_status)
        print(f"V - {duty}'s status updated.")
    except (KeyError, ValueError) as e:
        print(f"X -", e)

def handle_view_soldier_duties() -> None:
    try:
        soldier_id = int(input("Enter soldier's ID: ")) 
        duties = get_soldier_duties(soldier_id)
        if duties:
            print("Duties list:")
            for index, duty in enumerate(duties):
                print(f'\t{index + 1}. {duty["name"]} on {duty["day"]} - {duty["status"]}')
        else:
            print("There are not duties yet")
    except (KeyError, ValueError) as e:
        print(f"X -", e)

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