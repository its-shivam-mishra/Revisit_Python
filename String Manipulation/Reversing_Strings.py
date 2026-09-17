def reverse_string(s):
    return s[::-1] #string[start:end:step]    

#print(reverse_string("hello"))  # Output: "olleh"

def reverse_string_iterative(s):
    rev_str = ""
    for char in s:
        rev_str = char + rev_str
    return rev_str

print(reverse_string_iterative("hello1"))  # Output: "olleh"