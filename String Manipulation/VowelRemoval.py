def Vowelremovel(str):
    new_str = ""
    vowels=['a', 'e', 'i', 'o', 'u']
    for char in str:
        if char.lower() not in vowels:
            new_str += char 
    return new_str

print(Vowelremovel("Hello World"))  # Output: "Hll Wrld"