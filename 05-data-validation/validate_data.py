def validate_data(data: list | tuple) -> bool:
    for element in data:
        if type(element) is not int() or type(element) is not float():
            return False
        
        return True