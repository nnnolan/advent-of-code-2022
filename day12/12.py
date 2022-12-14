from string import ascii_lowercase
from heapq import heappop, heappush

with open ('12.txt') as f:
    lines = f.read().strip().split()

grid =[list(line) for line in lines]

n = len(grid)
m = len(grid[0])

for i in range(n):
    for j in range(m):
        char = [i][j]
        if char == 'S':
            start = (i, j)
        elif char == 'E':
            end = (i, j)

def height(s):
    if s in ascii_lowercase:
        return ascii_lowercase.index(s)
    if s == "S":
        return 0
    if s == "E":
        return 25
    
def neighbors(i, j):
    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ii = i + di
        jj = j + dj
        
        if not (0 <= ii < n and 0 <= jj < m):
            continue
            
        if height(grid[ii][jj]) <= height(grid[i][j]) + 1:
            yield ii,jj
        
#dijkstra's algorithm AGONY, PAIN, SUFFERING

visited = [[False * m for _ in range(n)]]
heap = [(0, start[0], start[1])]

while True:
    steps, i, j = heappop(heap)
    
    if visited[i][j]:
        continue
    
    visited[i][j] = True
    
    if (i,j) == end:
        print(steps)
        break
    
    for ii, jj in neighbors(i,j):
        heappush(heap,(steps + 1, ii, jj))
        
        
        #given a dataframe
        #two columns smilar shape and name 
        