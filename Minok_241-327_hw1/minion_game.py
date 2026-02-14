string = input()
vowels = set('AEIOU')
n = len(string)
if (len(string) > 1000 or len(string) == 0):
    print ('0 < len(string) <= 1000')

else:
    kevin = 0
    stuart = 0

    for i, char in enumerate(string):
        points = n - i
        
        if char in vowels:
            kevin += points
        else:
            stuart += points

    if kevin > stuart:
        print(f"Кевин {kevin}")
    elif stuart > kevin:
        print(f"Стюарт {stuart}")
