#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines of input. The first line contains two space-separated integers: the number of cows (n) and the index of the cow (k). The second line contains n space-separated integers representing the Cowdeforces ratings of the cows.
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    wins = 0
    for i in range(n):
        if a[i] > a[k - 1]:
            break
        
        wins += 1
        
    #State: wins is the number of integers in list a that are less than or equal to the integer at index k-1.
    if (wins >= k) :
        print(wins - 1)
        #This is printed: wins - 1 (where wins is the number of integers in list a that are less than or equal to the integer at index k-1, and the result is greater than or equal to k-1)
    #State: wins is the number of integers in list a that are less than or equal to the integer at index k-1, and if the current value of wins is greater than or equal to k, then the value of wins - 1 is printed.
    wins_with_swap = wins + 1
    for i in range(wins_with_swap, k - 1):
        if a[i] > a[k - 1]:
            break
        
        wins_with_swap += 1
        
    #State: Output State: `wins_with_swap` is the number of integers in list a that are less than or equal to the integer at index k-1 plus 1, and if the current value of wins is greater than or equal to k, then the value of wins - 1 is printed.
    print(max(wins - 1, wins_with_swap - wins - 1 + (wins > 0)))
    #This is printed: max(wins - 1, wins_with_swap - wins - 1 + (wins > 0)) (where wins_with_swap is the number of integers in list a that are less than or equal to the integer at index k-1 plus 1)

#Overall this is what the function does:Determines the maximum number of cows that can be defeated by a given cow in a competition, considering the possibility of swapping the given cow with a stronger one. The function takes no parameters and returns the maximum number of defeatable cows, which is either the number of cows with a rating less than or equal to the given cow's rating minus one, or the number of cows with a rating less than or equal to the given cow's rating plus one, minus the number of cows with a rating less than or equal to the given cow's rating, plus one if there are any cows with a rating less than or equal to the given cow's rating.

