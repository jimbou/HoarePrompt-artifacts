#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines of input. The first line contains two space-separated integers: the number of cows (n) and the index of the cow (k). The second line contains n space-separated integers representing the Cowdeforces ratings of the cows.
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    wins = 0
    for i in range(n):
        if a[i] > a[k - 1]:
            break
        
        wins += 1
        
    #State: `n` is an integer, `k` is an integer, `a` is a list of `n` integers, `wins` is the number of elements in `a` that are less than or equal to `a[k - 1]`, `stdin` contains multiple test cases minus 1, `i` is the index of the first element in `a` that is greater than `a[k - 1]` or `n` if no such element exists.
    if (wins >= k) :
        print(wins - 1)
        #This is printed: wins - 1 (where wins is the number of elements in the list a that are less than or equal to a[k - 1])
    #State: *`n` is an integer, `k` is an integer, `a` is a list of `n` integers, `wins` is the number of elements in `a` that are less than or equal to `a[k - 1]`, `stdin` contains multiple test cases minus 1, `i` is the index of the first element in `a` that is greater than `a[k - 1]` or `n` if no such element exists. If `wins` is greater than or equal to `k`, `wins - 1` is printed, where `wins - 1` is at least `k - 1`.
    wins_with_swap = wins + 1
    for i in range(wins_with_swap, k - 1):
        if a[i] > a[k - 1]:
            break
        
        wins_with_swap += 1
        
    #State: `n` is an integer, `k` is an integer, `a` is a list of `n` integers, `wins_with_swap` is the number of elements in `a` that are less than or equal to `a[k - 1]` plus the number of elements in the range from `wins_with_swap` to `k - 1` that are less than or equal to `a[k - 1]`, `wins` is the number of elements in `a` that are less than or equal to `a[k - 1]`, `stdin` contains multiple test cases minus 1, `i` is the index of the first element in `a` that is greater than `a[k - 1]` in the range from `wins_with_swap` to `k - 1` or `k - 1` if no such element exists.
    print(max(wins - 1, wins_with_swap - wins - 1 + (wins > 0)))
    #This is printed: max(wins - 1, wins_with_swap - wins) if wins > 0, otherwise max(wins - 1, wins_with_swap - wins - 1)

#Overall this is what the function does:This function determines the maximum number of wins a cow can achieve in a competition. It takes as input the number of cows (n) and the index of the cow (k), and a list of Cowdeforces ratings of the cows. The function calculates the number of wins the cow can achieve without swapping its rating with any other cow, and the number of wins it can achieve if it swaps its rating with the cow that has a higher rating. The function then prints the maximum of these two values. If the cow's original rating is not enough to achieve k wins, the function prints the maximum number of wins it can achieve with a rating swap, minus the number of wins it would have achieved without the swap, plus 1 if the cow had at least one win originally.

