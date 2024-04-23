def validate_pin(pin):
    if len(pin) == 4 and pin.isnumeric():
        return True
    if len(pin) == 6 and pin.isnumeric():
        return True
    else:
        return False