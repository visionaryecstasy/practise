s = "abcdefg"

def func(s):
    l = list(s)
    result = ""
    while len(l) > 0:
        result += l.pop()
    return result
result = func(s)
print(result)