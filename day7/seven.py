from collections import defaultdict
from functools import lru_cache

with open("seven.txt") as fin:
    blocks = ("\n" + fin.read().strip()).split("\n$ ")[1:]

dir_sizes = defaultdict(int)
children= defaultdict(list)
path = []
# print(lines)

def parse(block):
    lines = block.split("\n")
    command = lines[0]
    output = lines[1:]
    
    parts = command.split(" ")
    op = parts[0]
    
    if op == "cd":
        if parts[1] == "..": #going up a dir 
            path.pop() 
        else:
            path.append(parts[1]) #going down a dir
            
        return
    
    abspath = "/".join(path)
    
    assert op == "ls"
    
    total_size = []
    for line in output:
        if not line.startswith("dir"):
            total_size.append(int(line.split(" ")[0]))
        else:
            dir_name = line.split(" ")[1]
            children[abspath].append(f"{abspath}/{dir_name}")
    
    dir_sizes[abspath] = sum(total_size)
    
    for block in blocks:
        parse(block)

@lru_cache(None)
def dfs(abspath):
    size = dir_sizes[abspath]
    for child in children[abspath]:
        size += dfs(child)
    return size

total = 0
for abspath in dir_sizes:
    if dfs(abspath) <= 100000:
        total += dfs(abspath)
        
print(total)

# class Tree(object):
#     "Generic tree node."
#     def __init__(self, name='root', children=None):
#         self.name = name
#         self.children = []
#         if children is not None:
#             for child in children:
#                 self.add_child(child)
#     def __repr__(self):
#         return self.name
#     def add_child(self, node):
#         assert isinstance(node, Tree)
#         self.children.append(node)