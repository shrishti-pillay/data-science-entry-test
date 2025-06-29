def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) 
        and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    # Check if lst is a list 
    if not isinstance(lst, list):
        return "1st argument must be a list"

    # loop through each index of list, 
    # if the element of that index matches the find_val, 
    # store the replace_val in that index of the list

    for idx in range(0,len(lst)):
        if lst[idx] == find_val:
            lst[idx] = replace_val

    # Return updated lst
    return lst

# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
print(find_and_replace([1, 2, 3, 4, 2, 2], 2, 5))

# - ["apple", "banana", "apple"], "apple", "orange"
print(find_and_replace(["apple", "banana", "apple"], "apple", "orange"))
