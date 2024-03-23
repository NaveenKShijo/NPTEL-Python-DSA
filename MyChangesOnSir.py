



Data=["Zverev:Alcaraz:2-6,6-7,7-6,6-3,6-1",
"Swiatek:Jabeur:6-4,6-4",
"Alcaraz:Zverev:6-3,6-3",
"Jabeur:Swiatek:1-6,7-5,6-2",
"Zverev:Alcaraz:6-0,7-6,6-3",
"Jabeur:Swiatek:2-6,6-2,6-0",
"Alcaraz:Zverev:6-3,4-6,6-3,6-4",
"Swiatek:Jabeur:6-1,3-6,7-5",
"Zverev:Alcaraz:7-6,4-6,7-6,2-6,6-2",
"Jabeur:Swiatek:6-4,1-6,6-3",
"Alcaraz:Zverev:7-5,7-5",
"Jabeur:Swiatek:3-6,6-3,6-3"]



import re
player_stats = {}
for Var in Data:   

    Temp_1= re.split(':|,|-',Var)
    winner=Temp_1.pop(0)
    loser=Temp_1.pop(0)
    winner_score=[int(x) for x in Temp_1[::2]]  # Get elements at even indices & convert to int
    loser_score=[int(x) for x in Temp_1[1::2]]# Get elements at odd indices  & convert to int
    
    if winner not in player_stats:
        player_stats[winner] = [0, 0, 0, 0, 0, 0]  # [BO5 wins, BO3 wins, sets won, games won, sets lost, games lost]
    if loser not in player_stats:
        player_stats[loser] = [0, 0, 0, 0, 0, 0]    
    # Determine the type of match (BO5 or BO3) and update statistics accordingly
   
    if len(winner_score)>3:
        player_stats[winner][0] += 1  # BO5 wins
        player_stats[winner][2] += 3
        player_stats[loser][4] += 3    # Sets lost
        if len(winner_score) ==4:
            player_stats[winner][4] += 1   # sets lost
            player_stats[loser][2] += 1 #sets won
        else:
            player_stats[winner][4] += 2   # sets lost
            player_stats[loser][2] += 2 #sets won


    elif len(winner_score)==3:
        if(winner_score[0]>loser_score[0]) and (winner_score[1]>loser_score[1]) and (winner_score[2]>loser_score[2]):
            player_stats[winner][0] += 1 # BO5 wins
            player_stats[loser][4] += 3  # Sets lost  
            player_stats[winner][2] += 3 #sets won

        else:
            player_stats[winner][1] += 1  # BO3 wins
            player_stats[loser][4] += 2    # Sets lost   
            player_stats[winner][4] += 1    # Sets lost  
            player_stats[winner][2] += 2 #sets won
            player_stats[loser][2] += 1 #sets won
       
    
    else:
        player_stats[winner][1] += 1
        player_stats[winner][2] += 2
        player_stats[loser][4] += 2

    for i in range(len(winner_score)):
        #player_stats[winner][2] += 1  # Sets won
        player_stats[winner][3] += winner_score[i]  # Games won
        player_stats[loser][5] += winner_score[i]  # Games lost
        player_stats[loser][3] += loser_score[i]  # Games won
        player_stats[winner][5] += loser_score[i]  # Games lost    
            
print(player_stats,"\n\n")


stat_labels = ['BO5 wins', 'BO3 wins', 'Sets won', 'Games won', 'Sets lost', 'Games lost']