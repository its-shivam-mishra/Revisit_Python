def is_palindrome(s):
    return s == s[::-1] #string[start:end:step]

print(is_palindrome("madam"))   # True
print(is_palindrome("hello"))   # False


def is_palindrome_iterative(s):
    s2=''
    for char in s:
        s2=char+s2
    return s==s2

#print(is_palindrome_iterative("madam1"))   # True