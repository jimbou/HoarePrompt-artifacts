#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains two space-separated integers: the number of cows (n) and the index of the cow of interest (k). The second line contains n space-separated integers representing the Cowdeforces ratings of the cows.
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    wins = 0
    for i in range(n):
        if a[i] > a[k - 1]:
            break
        
        wins += 1
        
    #State: `n` is an integer, `k` is an integer, `a` is a list of `n` integers, `wins` is the number of integers in `a` that are less than or equal to `a[k - 1]`, stdin contains multiple test cases - 1. If `a` contains at least one integer greater than `a[k - 1]`, `i` is the index of the first such integer. If all integers in `a` are less than or equal to `a[k - 1]`, `i` is `n`.
    if (wins >= k) :
        print(wins - 1)
        #This is printed: k - 1 or more (where k - 1 is the minimum possible value of wins - 1)
    #State: *`n` is an integer, `k` is an integer, `a` is a list of `n` integers, `wins` is the number of integers in `a` that are less than or equal to `a[k - 1]`, stdin contains multiple test cases - 1. If `a` contains at least one integer greater than `a[k - 1]`, `i` is the index of the first such integer. If all integers in `a` are less than or equal to `a[k - 1]`, `i` is `n`. If the number of integers in `a` that are less than or equal to `a[k - 1]` is greater than or equal to `k`, the number of integers in `a` that are less than or equal to `a[k - 1]` minus 1 is being printed.
    wins_with_swap = wins + 1
    for i in range(wins_with_swap, k - 1):
        if a[i] > a[k - 1]:
            break
        
        wins_with_swap += 1
        
    #State: `n` is an integer, `k` is an integer greater than or equal to 2, `a` is a list of `n` integers, `wins` is the number of integers in `a` that are less than or equal to `a[k - 1]`, `wins_with_swap` is the number of integers in `a` that are less than or equal to `a[k - 1]` plus the number of integers in the range `[wins_with_swap, k - 1)` that are less than or equal to `a[k - 1]`, `i` is the index of the first integer in `a` that is greater than `a[k - 1]` in the range `[wins_with_swap, k - 1)` or `k - 1` if all integers in the range are less than or equal to `a[k - 1]`.
    print(max(wins - 1, wins_with_swap - wins - 1 + (wins > 0)))
    #This is printed: the maximum value between the count of elements in `a` that are less than or equal to the `k-1`th element of `a`, minus 1, and the count of additional elements in the range `[wins_with_swap, k - 1)` that are less than or equal to the `k-1`th element of `a`, minus 1, plus 1 if there are any elements in `a` that are less than or equal to the `k-1`th element of `a`

#Overall this is what the function does:The function reads input from stdin, processes multiple test cases, and prints the maximum number of wins for a cow of interest. For each test case, it reads the number of cows (n) and the index of the cow of interest (k), followed by the Cowdeforces ratings of the cows. It then calculates the number of wins for the cow of interest by counting the number of cows with ratings less than or equal to the cow of interest's rating. If the number of wins is greater than or equal to k, it prints the number of wins minus 1. Otherwise, it calculates additional wins by considering the range of cows from the number of wins plus 1 to k-1 and prints the maximum value between the count of elements less than or equal to the k-1th element minus 1 and the count of additional elements less than or equal to the k-1th element minus 1, plus 1 if there are any elements less than or equal to the k-1th element.

