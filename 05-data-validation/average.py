from validate_data import validate_data

def get_average(data: list | tuple ) -> float:
    if not validate_data(data):
        print("List or Tuple does not contain number")
        return None

    sum = 0
    
    for element in data:
        sum += element

    return sum / len(data)



