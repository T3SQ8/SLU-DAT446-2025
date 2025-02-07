def nth_largest_el(data: list | tuple, n: int):
    # Sort the list in descending order (reverse=True)
    data.sort(reverse=True)
    # Return the kth largest element (0-based index, so k-1)
    return data[n - 1]