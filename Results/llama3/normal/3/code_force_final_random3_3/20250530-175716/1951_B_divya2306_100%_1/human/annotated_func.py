#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains two space-separated integers: the number of cows (n) and the index of the cow (k). The second line contains n space-separated integers representing the Cowdeforces ratings of the cows. n is an integer such that 2 <= n <= 10^5, k is an integer such that 1 <= k <= n, and the Cowdeforces ratings are integers such that 1 <= a_i <= 10^9. The sum of n over all test cases does not exceed 10^5.
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    wins = 0
    for i in range(n):
        if a[i] > a[k - 1]:
            break
        
        wins += 1
        
    #State: `n` is an integer such that 2 <= n <= 10^5, `k` is an integer such that 1 <= k <= n, `a` is a list of n integers representing the Cowdeforces ratings of the cows, `wins` is the number of iterations of the loop, `stdin` contains multiple test cases minus 1, `i` is n. If `a[i]` is greater than `a[k - 1]`, the program breaks out of the most internal loop or if statement. Otherwise, no action is taken.
    if (wins >= k) :
        print(wins - 1)
        #This is printed: wins - 1 (where wins is the number of iterations of the loop and is greater than or equal to k)
        return
        #The program returns nothing, but the number of wins minus 1 is printed, where the number of wins is the number of iterations of the loop which is greater than or equal to k
    #State: *`n` is an integer such that 2 <= n <= 10^5, `k` is an integer such that 1 <= k <= n, `a` is a list of n integers representing the Cowdeforces ratings of the cows, `wins` is the number of iterations of the loop, `stdin` contains multiple test cases minus 1, `i` is n. The number of iterations of the loop (`wins`) is less than `k`. If `a[i]` is greater than `a[k - 1]`, the program breaks out of the most internal loop or if statement. Otherwise, no action is taken.
    win_with_swap = wins + 1
    for i in range(win_with_swap, k - 1):
        if a[i] > a[k - 1]:
            break
        
        win_with_swap += 1
        
    #State: `n` is an integer such that 2 <= n <= 10^5, `k` is an integer such that 1 <= k <= n, `a` is a list of n integers representing the Cowdeforces ratings of the cows, `wins` is the number of iterations of the loop, `win_with_swap` is increased by `wins`, `stdin` contains multiple test cases minus 1, `i` is `win_with_swap`. If `a[i]` is greater than `a[k - 1]`, then we break out of the most internal loop or if statement. Otherwise, no change occurs.
    print(max(wins - 1, win_with_swap - wins - 1 + (wins != 0)))
    #This is printed: the maximum of (wins - 1) and (the initial value of win_with_swap before the loop, minus one if wins is not zero, and minus zero if wins is zero)

#Overall this is what the function does:This function determines the maximum number of wins a cow can achieve in a competition, considering the possibility of swapping the cow's position with another cow. It takes the number of cows, the index of the cow, and the Cowdeforces ratings of the cows as input. The function prints the maximum number of wins the cow can achieve, either by maintaining its current position or by swapping with another cow. If the cow's current position is sufficient to achieve the required number of wins, the function prints the number of wins minus 1. Otherwise, it calculates the maximum number of wins the cow can achieve by swapping with another cow and prints the maximum of the two possible outcomes.

