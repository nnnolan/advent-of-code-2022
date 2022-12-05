
with open(r'five.txt') as x:
    x = x.readlines()
    lines = [item.strip() for item in x]
split_lines = []
for i in lines:
    split_lines.append(i.split(" "))
letters = []
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
                letters.append(j[count])
                count =+1
            elif j == "":
                letters.append("space")
            

    elif i[0] == "1":
        print("initial")
        pass
    elif i[0] == "move":
        print("move")
        pass



count = 1
for i in letters:
    print(i)
    if count == 1 and i != "space":
        one.append(i)
        count += 1
    
    elif count == 2 and i != "space":
        two.append(i)
        count += 1
    
    elif count == 3 and i != "space":
        three.append(i)
        count += 1
    
    elif count == 4 and i != "space":
        four.append(i)
        count += 1
    
    elif count == 5 and i != "space":
        five.append(i)
        count += 1
    
    elif count == 6 and i != "space":
        six.append(i)
        count += 1

    elif count == 7 and i != "space":
        seven.append(i)
        count += 1
    
    elif count == 8 and i != "space":
        eight.append(i)
        count = 1



print(one, two, three, four)
print(five, six, seven, eight)
