nums = [3,5,234,4,85,-23,4]
no_nums = []
empty = []


def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    if lst != empty:
        return lst[-1]
    else: 
        return None