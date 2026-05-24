from data import soldiers

def find_soldier_by_id(soldier_id: int) -> dict | None:
    for soldier in soldiers:
        if soldier['id'] == soldier_id:
            return soldier
    return None

def find_duty_by_name(duties: list, duty_name: str) -> dict | None:
    for duty in duties:
        if duty["name"] == duty_name:
            return duty
    return None

def is_valid_status(status: str) -> bool:
    valid_statuses = ['pending', 'completed', 'missed']
    return status.strip().lower() in valid_statuses

def is_valid_name(name: str) -> bool:
    return bool(name)

def soldier_has_duty(soldier: dict, duty_name: str) -> bool:
    for duty in soldier["duties"]:
        if duty["name"] == duty_name:
            return True
    return False

def is_valid_day(day: str) -> bool:
    valid_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
    return day.strip().capitalize() in valid_days