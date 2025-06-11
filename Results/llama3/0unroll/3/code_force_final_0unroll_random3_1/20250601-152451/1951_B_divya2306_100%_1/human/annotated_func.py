#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines of input. The first line contains two space-separated integers: the number of cows (n) and the index of the cow (k). The second line contains n space-separated integers representing the Cowdeforces ratings of the cows. The integers are pairwise different and are between 1 and 10^9.
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    wins = 0
    for i in range(n):
        if a[i] > a[k - 1]:
            break
        
        wins += 1
        
    #State: Output State: n is an integer, k is an integer, a is a list of n integers, wins is the number of elements in a that are less than or equal to a[k - 1], stdin contains multiple test cases - 1
    if (wins >= k) :
        print(wins - 1)
        #This is printed: wins - 1 (where wins is the number of elements in the list a that are less than or equal to the element at index k - 1 in the list a)
        return
        #The program returns nothing
    #State: *n is an integer, k is an integer, a is a list of n integers, wins is the number of elements in a that are less than or equal to a[k - 1], stdin contains multiple test cases - 1, and the number of elements in a that are less than or equal to a[k - 1] is less than k
    win_with_swap = wins + 1
    for i in range(win_with_swap, k - 1):
        if a[i] > a[k - 1]:
            break
        
        win_with_swap += 1
        
    #State: Output State: `win_with_swap` is the number of elements in `a` that are less than or equal to `a[k - 1]` and are in the range from index `wins` to `k - 1`.
    print(max(wins - 1, win_with_swap - wins - 1 + (wins != 0)))
    #This is printed: The maximum value between the number of elements in `a` that are less than or equal to `a[k - 1]` and are in the range from index `0` to `wins - 1` and the number of elements in `a` that are less than or equal to `a[k - 1]` and are in the range from index `wins` to `k - 1`, minus the number of elements in `a` that are less than or equal to `a[k - 1]` and are in the range from index `0` to `wins - 1`, minus 1, plus 1 if `wins` is not equal to 0

#Overall this is what the function does:This function determines the maximum number of wins a cow can achieve in a competition by either not swapping its position or swapping with another cow. It takes the number of cows (n) and the index of the cow (k) as input, along with the ratings of all cows. The function then calculates the number of wins the cow can achieve without swapping and the number of wins it can achieve by swapping with another cow. Finally, it prints the maximum number of wins the cow can achieve in either scenario, considering the case where the cow's rating is not the highest among the first k cows.

