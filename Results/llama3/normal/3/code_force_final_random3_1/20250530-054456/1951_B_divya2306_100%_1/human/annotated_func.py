#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains two space-separated integers: the number of cows (n) and the index of the cow (k). The second line contains n space-separated integers representing the Cowdeforces ratings of the cows.
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    wins = 0
    for i in range(n):
        if a[i] > a[k - 1]:
            break
        
        wins += 1
        
    #State: `n` is a positive integer, `i` is `n`, `k` is an integer, `a` is a list of `n` integers, `wins` is the number of elements in `a` that are less than or equal to `a[k - 1]`, `stdin` contains multiple test cases - 1.
    if (wins >= k) :
        print(wins - 1)
        #This is printed: wins - 1 (where wins is the number of elements in the list a that are less than or equal to a[k - 1], and is at least k - 1)
        return
        #The program returns nothing
    #State: *`n` is a positive integer, `i` is `n`, `k` is an integer, `a` is a list of `n` integers, `wins` is the number of elements in `a` that are less than or equal to `a[k - 1]`, `stdin` contains multiple test cases - 1, and `wins` is less than `k`
    win_with_swap = wins + 1
    for i in range(win_with_swap, k - 1):
        if a[i] > a[k - 1]:
            break
        
        win_with_swap += 1
        
    #State: `n` is a positive integer, `i` is `k`, `k` is an integer, `a` is a list of `n` integers, `wins` is less than `k`, `win_with_swap` is `wins` plus the number of elements in `a` from index `wins` to `k - 1` that are less than or equal to `a[k - 1]`.
    print(max(wins - 1, win_with_swap - wins - 1 + (wins != 0)))
    #This is printed: The maximum value between [wins - 1] and the number of elements in `a` from index `wins` to `k - 1` that are less than or equal to `a[k - 1]`, or the number of elements in `a` from index `wins` to `k - 1` that are less than or equal to `a[k - 1]`, plus 1 if `wins` is not equal to 0

#Overall this is what the function does:The function determines the maximum number of wins a cow can achieve in a competition, given its rating and the ratings of other cows. It takes as input the number of cows, the index of the cow, and the ratings of all cows. The function then calculates the number of wins the cow can achieve without swapping its rating with any other cow, and the number of wins it can achieve if it swaps its rating with the cow at the next higher rating. The function prints the maximum of these two values, minus one if the cow's original rating is not the highest, and returns nothing.

