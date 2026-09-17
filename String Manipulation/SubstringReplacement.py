def substring_replacement(s, old, new):
    result = ""
    i = 0

    while i < len(s):
        if s[i:i + len(old)] == old:
            result += new
            i += len(old)
        else:
            result += s[i]
            i += 1

    return result





def substring_replacement_builtin(s, old, new):
    return s.replace(old, new)  

def substring_rep(s, old, new):
    result=""
    for i in s.split():
        if i==old:
            result+=new+" "
        else:
            result+=i+" "
    return result


# Example
s = "I love Python. Python is easy."
print(substring_rep(s, "Python", "C#"))