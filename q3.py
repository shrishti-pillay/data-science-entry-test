def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """

    # Check if the key already exists in dct
    if dct.get(key, None) is not None: 
        # If yes, then print the key and original value
        print(f'{key=}: original value={dct[key]}')
    
    # Set new value for that attribute
    dct[key] = value

    # Return updated dct
    return dct


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
print(update_dictionary({}, "name","Alice"))

# - {"age": 25}, "age", 26
print(update_dictionary( {"age": 25}, "age", 26))
