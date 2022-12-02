with open(r'C:\Users\npestano\Documents\GitHub\advent-of-code-2022\advent-of-code-2022\day2\two.txt') as f:
    x = f.readlines()
    lines = [item.strip() for item in x]



total = 0

#x = lose y = draw z = win

for i in lines:

    if i[2] == "X": # lose case    
        
        if i[0] == "A": #lose, opponent gives rock, i   respond scissors
            total += 3
        
        elif i[0] == "B": #lose, opponent gives paper, i respond rock
            total +=1 
        
        elif i[0] == "C": #lose, opponent gives scissors, i respond paper
            total += 2
            
           
    
    elif i[2] == "Y": # DRAWS
        
        if i[0] == "A": #draw, opponent gives rock, i respond rock
            total +=4
        
        elif i[0] == "B": #draw, opponent gives paper, i respond paper
            total += 5
        
        elif i[0] == "C": #draw, opponent gives scissors, i respond scissors
            total += 6

    
    elif i[2] == "Z": # need to win

        if i[0] == "A": #win, opponent gives rock, i respond paper
            total += 8
        
        if i[0] == "B": #win, opponent gives paper, i respond scissors
            total += 9
        
        if i[0] == "C": #win, opponent gives scissors, i respond rock
            total += 7
            
print(total)        

