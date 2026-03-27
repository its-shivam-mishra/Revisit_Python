#Write a function to determine if two strings are anagrams of each other (e.g., "listen" and "silent").

def check_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Sort the characters of both strings and compare
    return sorted(str1) == sorted(str2) 


#Manual Frequency Count

def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Create frequency dictionaries for both strings
    freq1 = {}
    freq2 = {}
    
    for char in str1:
        freq1[char] = freq1.get(char, 0) + 1
        print(freq1[char])
        
    for char in str2:
        freq2[char] = freq2.get(char, 0) + 1
        
    # Compare the frequency dictionaries
    return freq1 == freq2

# Example usage
string1 = "listenn"      
string2 = "silent"
print(are_anagrams(string1, string2))  # Output: True
#print(check_anagrams(string1, string2))  # Output: True
