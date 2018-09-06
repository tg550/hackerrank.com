# Complete the p1_win_count function below.

def p1_win_count(hands):
    import statistics
    n=0
    p1 = hands[0][:3]
    p2 = hands[0][3:]
    ##check player1
    if (p1[0] == p1[1]) or (p1[1] == p1[2]) or (p1[0] == p1[2]):
        if (p1[0] == p1[1]) and (p1[1] == p1[2]):
            player1_rank = 3
        else:
            player1_rank = 2
    else:
        player1_rank = 1    
    ##check player2
    if (p2[0] == p2[1]) or (p2[1] == p2[2]) or (p2[0] == p2[2]):
        if (p2[0] == p2[1]) and (p2[1] == p2[2]):
            player2_rank = 3
        else:
            player2_rank = 2
    else:
        player2_rank = 1 
    #compare players' rank
    if player1_rank > player2_rank:
        n = n+1
    elif player1_rank == player2_rank:
        if player1_rank == 1:
            if max(p1) > max(p2):
                n=n+1
            elif (max(p1) == max(p2)) and (statistics.median(p1) > statistics.median(p2)):
                n=n+1
            elif (max(p1) == max(p2)) and (statistics.median(p1) == statistics.median(p2)) and (min(p1)>min(p2)):
                n=n+1
            else:
                n=0
        elif player1_rank == 2:
            if max(p1,key=p1.count) > max(p2,key=p2.count):
                n = n+1
            elif max(p1,key=p1.count) == max(p2,key=p2.count):
                if min(p1,key=p1.count) > min(p2,key=p2.count):
                    n=n+1
            else:
                n=0
        elif player1_rank == 3:
            if max(p1) > max(p2):
                n = n+1
        else:
            n=0
    return n
        
        
        
        


p1_win_count([[8, 2, 3, 4, 3, 6]])
