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
        if j in secondpart and j not in currently_checking:
            print(f"found a match: {j}, {secondpart}")
            currently_checking.append(j)
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

#part two , part one is beyond repair
#this won't be pretty
test = 0
splits = [lines[i:i+3] for i in range(0,len(lines),3)]

currently_checking = []
total = 0
alphabets=list(string.ascii_letters)

for i in splits:
    print(i)
    currently_checking = []
    for j in alphabets:
        if j in i[0] and j in i[1] and j in i[2] and j not in currently_checking:
            currently_checking.append(j)
            total += alphabetvalues[j]
            print(f"found a match: {j}, {i}")
            print(currently_checking)
print(total)

