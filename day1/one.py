with open(r'C:\Users\npestano\Documents\GitHub\advent-of-code-2022\advent-of-code-2022\day1\day1.txt') as f:
    lines = f.readlines()

print(lines)
largest = 0
largest2 = 0
largest3 = 0
current_checking = 0
for i in lines:
    try:
        current_checking += int(i)
    
    except ValueError:
        print("ValueError")
        if current_checking > largest:
            largest = current_checking
        elif current_checking > largest2:
            largest2 = current_checking
        elif current_checking > largest3:
            largest3 = current_checking
        
        current_checking = 0
        
print(largest)

print(largest + largest2 + largest3)
        
    
        
