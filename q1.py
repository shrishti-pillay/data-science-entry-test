def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """

    # This approach assumes that if x or y is set as "10", 
        # it is also acceptable as it can be converted to int using casting
        # But if x = "Apple" it will return -1
    try: 
        x = int(x)
        y = int(y)
    except Exception:
        return -1

    # Store x in temp var
    # Set x as y
    # Set y as temp value
    temp = x
    x = y
    y = temp

    # Print updated x and y values
    return f"Swapped values {x=},{y=}"

# Task 2
# Invoke the function "swap" using the following scenarios:

# - "Apple", 10
x = "Apple"
y = 10
print(swap(x,y))

# - 9, 17
x = 9
y = 17
print(swap(x,y))



