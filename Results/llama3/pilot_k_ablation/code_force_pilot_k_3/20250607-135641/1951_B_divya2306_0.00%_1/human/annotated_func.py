#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines of input. The first line contains two integers n and k (2 <= n <= 10^5, 1 <= k <= n). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    wins = 0
    for i in range(n):
        if a[i] > a[k - 1]:
            break
        
        wins += 1
        
    #State: `n` and `k` are integers, `a` is a list of `n` integers, `wins` is `n`, stdin contains multiple test cases minus one, `n` is greater than or equal to 0, `i` is `n-1`. If `a[i]` is greater than `a[k - 1]`, the program breaks out of the most internal loop or if statement. Otherwise, no change occurs.
    if (wins >= k) :
        print(wins - 1)
        #This is printed: n-1 (where n is an integer greater than or equal to 0)
    #State: *`n` and `k` are integers, `a` is a list of `n` integers, `wins` is `n`, stdin contains multiple test cases minus one, `n` is greater than or equal to 0, `i` is `n-1`. If `a[i]` is greater than `a[k - 1]`, the program breaks out of the most internal loop or if statement. Otherwise, no change occurs. If `wins` is greater than or equal to `k`, the value of `wins - 1` is being printed.
    wins_with_swap = wins + 1
    for i in range(wins_with_swap, k - 1):
        if a[i] > a[k - 1]:
            break
        
        wins_with_swap += 1
        
    #State: `n` and `k` are integers, `a` is a list of `n` integers, `wins_with_swap` is less than or equal to `k` and is equal to `wins + k - 1`, `stdin` contains multiple test cases minus one, `n` is greater than or equal to 0, `i` is `k - 1`. If `a[i]` is greater than `a[k - 1]`, the program breaks out of the most internal loop or if statement. Otherwise, no changes are made.
    print(max(wins - 1, wins_with_swap - wins - 1 + (wins > 0)))
    #This is printed: max(wins - 1, k - 2 + (wins > 0)) (where wins is the value of wins and k is the value of k)

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of two lines: the first line contains two integers n and k, and the second line contains n integers. The function calculates the number of wins (wins) by iterating through the list of integers and comparing each element to the kth element. If wins is greater than or equal to k, it prints wins - 1. Otherwise, it calculates an additional number of wins (wins_with_swap) by iterating through the list again, starting from the wins + 1 index, and prints the maximum of wins - 1 and wins_with_swap - wins - 1 + (wins > 0). The function effectively determines the maximum number of wins that can be achieved by swapping the kth element with another element in the list, and prints this value for each test case.

