from math import floor 

def get_median(data: list | tuple) -> float:
    data.sort()

    if len(data) % 2 == 0:
        sum_middle_elements = data[int(len(data)/2)-1] + data[int(len(data)/2)]
        return sum_middle_elements/2

    return data[floor(len(data)/2)]