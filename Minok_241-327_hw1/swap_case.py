s = input()
if (len(s) > 1000 or len(s) == 0):
    print ('0 < len(string) <= 1000')
else:
    result = ''
    for char in s:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char
    print(result)