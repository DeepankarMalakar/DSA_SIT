# E. Write a function that takes a string as a parameter and returns a string
# with every successive repetitive character replaced with a star(*). For
# example, ‘balloon’ is returned as ‘bal*o*n’.

def replace_repetitive(s):
    result = ""
    for char in s:
        if s.count(char) > 1:
            if char not in result:
                result += char + "*"
        else:
            result += char
    return result

print(replace_repetitive("balloon"))
