# Find the longest substring without repeating characters

def longest_substring_without_repeating_characters(s):
    str=""
    for i in s.split():
        if len(str)<len(i):
            lst=[]
            for char in i:
                if char not in lst:
                    lst.append(char)
                else:
                    break
            str="".join(lst)
    return str
    
    
print(longest_substring_without_repeating_characters("Hello my name is shivam"))
    
    