from utils import *

def add_soldier(soldier_id: int, name: str) -> None:
    if not (is_valid_name(name) and find_soldier_by_id(id)):
        raise ValueError
    soldiers.append({'id': soldier_id, "name": name, "duties": []})


def remove_soldier(soldier_id: int) -> None:
    soldier = find_soldier_by_id(id)
    if not soldier:
        raise KeyError
    soldiers.remove(soldier)

def get_all_soldiers() -> list:
    return soldiers