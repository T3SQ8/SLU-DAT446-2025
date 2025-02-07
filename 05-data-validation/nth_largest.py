from validate_data import validate_data

def nth_largest_el(data: list | tuple, n: int):
    if not validate_data(data):
        print("List or Tuple does not contain number")
        return None
    
    if len(data) == 0: 
        print("List or Tuple is empty")
        return None
    

    if n > len(data)-1:
        print("n is too large for given list or tuple")
        return None

    # Sort the list in descending order (reverse=True)
    data.sort(reverse=True)
    # Return the kth largest element (0-based index, so k-1)
    return data[n - 1]