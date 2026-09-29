# Find the longest palindromic substring
'''
this is for word in string, not for substring in string
'''

def longest_palindromic_word(s):
    str=""
    for w in s.split():
        for char in w:
            if w[::-1]==w:
                if len(str)<len(w):
                    str=w
        
    return str
    
#print(longest_palindromic_substring("hello every ono and madam what"))


# Find the longest palindromic substring
def longest_palindromic_substring(s):
    str=""
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            sub=s[i:j]
            if sub==sub[::-1]:
                if len(str)<len(s[i:j]):
                    str=s[i:j]
    return str
            
            
            
        

print(longest_palindromic_substring("babad"))