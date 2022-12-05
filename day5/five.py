
with open(r'five.txt') as x:
    x = x.readlines()
    lines = [item.strip() for item in x]
split_lines = []
for i in lines:
    split_lines.append(i.split(" "))

one = []
two = []
three = []
four = []
five = []
six = []
seven = []
eight = []

for i in split_lines:
    if i[0] != "move" and i[0] != "1":
        count = 1
        for j in i:
            print(j)
            if count == 1 and "[" in j:
                one.append(j[count])
                count =+1
            elif count == 2 and "[" in j:
                two.append(i[2])
                count += 1
    elif i[0] == "1":
        print("initial")
        pass
    elif i[0] == "move":
        print("move")
        pass

print(one, two)
