def reverse_string(s):
    return s[::-1] #string[start:end:step]    

#print(reverse_string("hello"))  # Output: "olleh"

def reverse_string_iterative(s):
    rev_str = ""
    for char in s:
        rev_str = char + rev_str
    return rev_str

#print(reverse_string_iterative("hello shivam"))  # Output: "olleh"

def xyz(s):
    str=""
    line=s.split(" ")
    for i in line:
        str=i[::-1]+" "+str
    return str
    
print(xyz("hello shivam"))