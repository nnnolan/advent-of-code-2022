
with open(r'C:\Users\Nolan\Documents\GitHub\advent-of-code-2022\day4\four.txt') as f:
    x = f.read().strip()

lines = x.split('\n')

# print(lines)
count = 0
parttwo = 0
for i in lines:
    a, b = i.split(',')
    
    a1, a2 = map(int, a.split('-'))
    
    b1, b2 = map(int, b.split('-'))
    
    if a1 <= b1 <= b2 <= a2 or (
        b1 <= a1 <= a2 <= b2
    ):
        count += 1
        
