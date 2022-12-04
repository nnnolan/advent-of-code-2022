import string

with open(r'C:\Users\Nolan\Documents\GitHub\advent-of-code-2022\day3\three.txt') as f:
    x = f.readlines()
    lines = [item.strip() for item in x]

systems = []
for i in lines:
    currently_checking = []
    firstpart, secondpart = i[:len(i)//2], i[len(i)//2:]
    if len(firstpart) != len(secondpart):
        print("something went wrong you idiot")
        break
    for j in firstpart:
        print(firstpart, secondpart)
        if j in secondpart and j not in currently_checking:
            print(f"found a match: {j}, {secondpart}")
            currently_checking.append(j)
            print(currently_checking)
            systems.append(j)


print(systems)

lowercase_alphabets=list(string.ascii_lowercase)
uppercase_alphabets=list(string.ascii_uppercase)

alphabetvalues = {}

for i in range(len(lowercase_alphabets)):
    alphabetvalues[lowercase_alphabets[i]] = i+1
    alphabetvalues[uppercase_alphabets[i]] = i+27
print(alphabetvalues)

total = 0
for i in systems:
    total += alphabetvalues[i]

print(total)
    