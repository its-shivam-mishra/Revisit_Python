def character_frequency(str1):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    
    # Create frequency dictionaries for both strings
    freq1 = {}
    
    for char in str1:
        freq1[char] = freq1.get(char, 0) + 1
       
        
    # Compare the frequency dictionaries
    return freq1

# Example usage
string1 = "listenN"  
print(character_frequency(string1))  # Output: True