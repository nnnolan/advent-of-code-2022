with open('seven.txt') as x:
    x = x.readlines()
    lines = [item.strip() for item in x]
    
dirs = []
# print(lines)
for i in lines:
    if i.startswith('$ cd /'): # base dir
        pass
    
    if i.startswith('dir'):
        new = i.split()
        print(new)
        name = new[1]
        dirs.append(name)
        
    
    if i.startswith('$ ls'):
        pass
print(dirs)