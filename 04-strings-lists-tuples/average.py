def get_average(data: list | tuple ) -> float:
    sum = 0
    
    for element in data:
        sum += element

    return sum / len(data)