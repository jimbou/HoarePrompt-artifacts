#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains two integers: the number of cows (n) and the index of the cow of interest (k). The second line contains a list of n integers representing the Cowdeforces ratings of the cows.
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    wins = 0
    for i in range(n):
        if a[i] > a[k - 1]:
            break
        
        wins += 1
        
    #State: `n` is an integer, `k` is an integer, `a` is a list of `n` integers, `wins` is equal to the number of elements in `a` that are less than or equal to `a[k - 1]`, stdin contains multiple test cases - 1, `i` is equal to `n`.
    if (wins >= k) :
        print(wins - 1)
        #This is printed: wins - 1 (where wins is the number of elements in the list a that are less than or equal to the element at index k - 1 in the list a)
    #State: *`n` is an integer, `k` is an integer, `a` is a list of `n` integers, `wins` is equal to the number of elements in `a` that are less than or equal to `a[k - 1]`, stdin contains multiple test cases - 1, `i` is equal to `n`. If the current value of `wins` is greater than or equal to `k`, the value of `wins - 1` is being printed.
    wins_with_swap = wins + 1
    for i in range(wins_with_swap, k - 1):
        if a[i] > a[k - 1]:
            break
        
        wins_with_swap += 1
        
    #State: `n` is an integer, `k` is an integer greater than `wins_with_swap`, `a` is a list of `n` integers, `wins` is equal to the number of elements in `a` that are less than or equal to `a[k - 1]`, `wins_with_swap` is equal to `wins + k - wins` and less than or equal to `k - 1`, `i` is equal to `k - 1`. If `a[i]` is greater than `a[k - 1]`, the program breaks out of the most internal loop or if statement. Otherwise, no action is taken.
    print(max(wins - 1, wins_with_swap - wins - 1 + (wins > 0)))
    #This is printed: max(wins - 1, wins_with_swap - wins)

#Overall this is what the function does:This function determines the maximum number of wins a cow can achieve in a competition. It takes as input the number of cows (n) and the index of the cow of interest (k), as well as a list of Cowdeforces ratings for each cow. The function then calculates the number of wins the cow of interest can achieve without swapping its rating with any other cow, and the number of wins it can achieve if it swaps its rating with the cow that has the highest rating among the cows with lower ratings. The function prints the maximum of these two values, which represents the maximum number of wins the cow of interest can achieve.

