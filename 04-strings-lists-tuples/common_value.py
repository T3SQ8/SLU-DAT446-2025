def get_common_character(data: str) -> str:
    list_data = list(data)
    return get_common_value(list_data)


def get_common_value(data: list | tuple) -> float:
    register = dict()
    
    for element in data:
        if element not in register.keys():
            register[element] = 1
            continue

        register[element] += 1


    sorted_elements = sorted(register.items(), key=lambda x:x[1], reverse=True)
    
    return sorted_elements[0][0]