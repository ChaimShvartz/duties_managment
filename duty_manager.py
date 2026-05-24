from utils import *

def add_duty_to_soldier(soldier_id: int, duty_name: str, day: str) -> None:
    soldier = find_soldier_by_id(soldier_id)
    if not soldier:
        raise KeyError(f"Soldier with ID {soldier_id} not found.")
    if not is_valid_day(day):
        raise ValueError(f"{day} is an invalid day.")
    if soldier_has_duty(soldier, duty_name):
        raise ValueError(f"The soldier has already {duty_name} duty.")
    soldier["duties"].append({"name": duty_name, "day": day, "status": "pending"})

def update_duty_status(soldier_id: int, duty_name: str, new_status: str) -> None:
    soldier = find_soldier_by_id(soldier_id)
    if not soldier:
        raise KeyError(f"Soldier with ID {soldier_id} not found.")
    duty = find_duty_by_name(soldier["duties"], duty_name)
    if not duty:
        raise KeyError(f"{duty_name} not found.")
    if not is_valid_status(new_status):
        raise ValueError(f"{new_status} is an invalid status.")
    duty["status"] = new_status

def get_soldier_duties(soldier_id: int) -> list:
    soldier = find_soldier_by_id(soldier_id)
    if not soldier:
        raise KeyError(f"Soldier with ID {soldier_id} not found.")
    return soldier["duties"]