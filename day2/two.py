with open(r'C:\Users\npestano\Documents\GitHub\advent-of-code-2022\advent-of-code-2022\day2\two.txt') as f:
    x = f.readlines()
    lines = [item.strip() for item in x]



total = 0

#x = lose y = draw z = win

for i in lines:

    if i[0] == "A": # OPPONET GIVES ROCK
        
        if i[2] == "X":#ROCK V ROCK
            total += 4
            
        elif i[2] == "Y":#ROCK V PAPER
            total += 8
        
        elif i[2] == "Z": # ROCK V SCISSORS
            total += 3
    
    elif i[0] == "B": # OPPONET GIVES PAPER
        
        if i[2] == "X": #PAPER V ROCK
            total += 1 
            
        elif i[2] == "Y": #PAPER V PAPER
            total += 5
            
        elif i[2] == "Z": #PAPER V SCISSORS
            total += 9
    
    elif i[0] == "C": # OPPONET GIVES SCISSORS
        
        if i[2] == "X": #SCISSORS V ROCK
            total += 7
        
        elif i[2] == "Y": #SCISSORS V PAPER
            total += 2
        
        elif i[2] == "Z":  #SCISSORS V SCISSORS
            total += 6
            
print(total)        

