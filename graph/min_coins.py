def min_coins(coins, S):
    #initialize an array to store M with a large value
    M = [float('inf')] * (S + 1)
    
    #Base case: 0 coins are needed to form sum 0
    M[0] = 0

    #compute the minimum coins needed for each sum from 1 to S
    for i in range(1, S + 1):
        for coin in coins: 
            if i >= coin:
                #eg i = 6 coin = 5;so M[6] = 1 + M[6-5] = 1+ M[1]
                M[i] = min(M[i], 1 + M[i - coin])
    
    return M[S] if M[S] != float('inf') else -1


#example usage
coins = [1, 5, 12]
S = 14

result = min_coins(coins, S)
print(f"minimum coins required to form sum {S}: {result} ")

'''
output:
minimum coins required to form sum 15: 3 
minimum coins required to form sum 16: 4 
minimum coins required to form sum 14: 3 
'''