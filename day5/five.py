with open('five.txt') as x:
    x = x.readlines()
    lines = [item.strip() for item in x]
split_lines = []
for i in lines:
    split_lines.append(i.split(" "))
letters = []
one = ['W', 'B', 'G', 'Z', 'R', 'D', 'C', 'V']
two = ['V', 'T', 'S', 'B', 'C', 'F', 'W' ,'G']
three = ['W', 'N', 'S', 'B', 'C']
four = ['P', 'C', 'V', 'J', 'N', 'M', 'G', 'Q']
five = ['B', 'H', 'D', 'F', 'L', 'S', 'T']
six = ['N', 'M', 'W', 'T', 'V', 'J']
seven = ['G', 'T', 'S', 'C', 'L', 'F', 'P']
eight = ['Z', 'D', 'B']
nine = ['W', 'Z', 'N', 'M']

one.reverse()
two.reverse()
three.reverse()
four.reverse()
five.reverse()
six.reverse()
seven.reverse()
eight.reverse()
nine.reverse()

def where_to(where_to_move):
    if where_to_move == 1:
        return one
    if where_to_move == 2:
        return two
    if where_to_move == 3:
        return three
    if where_to_move == 4:
        return four
    if where_to_move == 5:
        return five
    if where_to_move == 6:
        return six
    if where_to_move == 7:
        return seven
    if where_to_move == 8:
        return eight
    if where_to_move == 9:
        return nine


for i in split_lines:
    
    temp = []
    
    if 'move' in i:
        print(i)
        
        count_to_move = int(splitted[1])
        where_to_move = int(splitted[5])
        from_to_move = int(splitted[3])
        
        if from_to_move == 1:
            for i in range(count_to_move):
                temp.append(one.pop())
                dest = where_to(where_to_move)
                print(dest)
             

        
# for i in split_lipes:
#     print(i)
#     if i[0] != "move" and i[0] != "1": # setup
#         count = 1
#         for j in i:
#             if count == 1 and "[" in j:
#                 letters.append(j[count])
#                 count =+1
#             elif j == "":
#                 letters.append("space")
            

#     elif i[0] == "1": #initial
#         pass
#     elif i[0] == "move": #move
#         pass



# count = 1
# for i in letters:
#     print(i)
    
#     if i == "space":
#         if count != 9:
#             print("space and count is not 9")
#             print(f"count is {count}, before addition")
#             count +=1
#         else:
#             print("space and count = 9")
#             count = 1
        
#     if count == 1 and i != "space":
#         one.append(i)
#         print(f"one: {one}, count: {count}, i: {i}")
#         count += 1
    
#     elif count == 2 and i != "space":
#         two.append(i)
#         print(f"two: {two}, count: {count}, i: {i}")
#         count += 1
    
#     elif count == 3 and i != "space":
#         three.append(i)
#         print(f"three: {three}, count: {count}, i: {i}")
#         count += 1
    
#     elif count == 4 and i != "space":
#         print(f"four: {four}, count: {count}, i: {i}")
#         four.append(i)
#         count += 1
    
#     elif count == 5 and i != "space":
#         print(f"five: {five}, count: {count}, i: {i}")
#         five.append(i)
#         count += 1
    
#     elif count == 6 and i != "space":
#         print(f"six: {six}, count: {count}, i: {i}")
#         six.append(i)
#         count += 1

#     elif count == 7 and i != "space":
#         print(f"seven: {seven}, count: {count}, i: {i}")
#         seven.append(i)
#         count += 1
    
#     elif count == 8 and i != "space":
#         print(f"eight: {eight}, count: {count}, i: {i}")
#         eight.append(i)
#         count += 1
        
#     elif count == 9 and i != "space":
#         print(f"nine: {nine}, count: {count}, i: {i}")
#         nine.append(i)
#         count = 1


print(one, two, three, four)
print(five, six, seven, eight)
