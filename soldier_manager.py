from utils import *

def add_soldier(soldier_id: int, name: str) -> None:
    if not is_valid_name(name):
        raise ValueError("The name must be non-empty.")
    if find_soldier_by_id(soldier_id):
        raise ValueError(f"ID {soldier_id} is already in used.")
    soldiers.append({'id': soldier_id, "name": name, "duties": []})

def remove_soldier(soldier_id: int) -> None:
    soldier = find_soldier_by_id(soldier_id)
    if not soldier:
        raise KeyError(f"Soldier with ID {soldier_id} not found.")
    soldiers.remove(soldier)

def get_all_soldiers() -> list:
    return soldiers