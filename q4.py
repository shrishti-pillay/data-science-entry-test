def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    # Check if s is a string
    if not isinstance(s, str):
        return "s should be a string."
    
    # 1. Convert s to a list
    # 2. Reverse the items
    # 3. Join them back
    return ''.join(list(s)[::-1])


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
print(string_reverse("Hello World"))
# - "Python"
print(string_reverse("Python"))