with open('six.txt') as x:
    x = x.readlines()
    lines = [item.strip() for item in x]
long_string = ''.join(lines)

print(long_string)

amount = 0

while amount == 0:
    for i in range(len(long_string)):
        current = ""
        
        for j in [0,1,2,3]:
            if long_string[j+i] in current:
                break

            else:
                current += long_string[j+i]
            
        if len(current) == 4:
            amount = i+j+1
            break
print(amount)


# two

amount = 0

while amount == 0:
    for i in range(len(long_string)):
        current = ""
        
        for j in [0,1,2,3,4,5,6,7,8,9,10,11,12,13]:
            if long_string[j+i] in current:
                break

            else:
                current += long_string[j+i]
            
        if len(current) == 14:
            amount = i+j+1
            break

print(f'second = {amount}')