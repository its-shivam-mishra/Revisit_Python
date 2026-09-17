def is_palindrome(s):
    return s == s[::-1] #string[start:end:step]

print(is_palindrome("madam"))   # True
print(is_palindrome("hello"))   # False


