#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines of input. The first line contains two integers n and k (2 <= n <= 10^5, 1 <= k <= n). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    wins = 0
    for i in range(n):
        if a[i] > a[k - 1]:
            break
        
        wins += 1
        
    #State: `n` is an integer, `k` is an integer, `a` is a list of `n` integers, `wins` is the number of integers in `a` that are less than or equal to `a[k - 1]`, `stdin` contains multiple test cases minus 1, `i` is either `n` or the index of the first integer in `a` that is greater than `a[k - 1]`.
    if (wins >= k) :
        print(wins - 1)
        #This is printed: at least k - 1 (where k is the given integer)
    #State: *`n` is an integer, `k` is an integer, `a` is a list of `n` integers, `wins` is the number of integers in `a` that are less than or equal to `a[k - 1]`, `stdin` contains multiple test cases minus 1, `i` is either `n` or the index of the first integer in `a` that is greater than `a[k - 1]`. If the number of integers in `a` that are less than or equal to `a[k - 1]` is greater than or equal to `k`, then the value of `wins - 1` is being printed.
    wins_with_swap = wins + 1
    for i in range(wins_with_swap, k - 1):
        if a[i] > a[k - 1]:
            break
        
        wins_with_swap += 1
        
    #State: `n` is an integer, `k` is an integer, `a` is a list of `n` integers, `wins` is the number of integers in `a` that are less than or equal to `a[k - 1]`, `wins_with_swap` is the number of integers in `a` that are less than or equal to `a[k - 1]` plus the number of integers in `a` from index `wins` to `k - 1` that are less than or equal to `a[k - 1]`, `stdin` contains multiple test cases minus 1, `i` is either `n` or the index of the first integer in `a` that is greater than `a[k - 1]`. If the number of integers in `a` that are less than or equal to `a[k - 1]` is greater than or equal to `k`, then the value of `wins - 1` is being printed.
    print(max(wins - 1, wins_with_swap - wins - 1 + (wins > 0)))
    #This is printed: The maximum of wins - 1 and wins_with_swap - wins - 1 + (wins > 0) (where wins is the number of integers in a that are less than or equal to a[k - 1], wins_with_swap is the number of integers in a that are less than or equal to a[k - 1] plus the number of integers in a from index wins to k - 1 that are less than or equal to a[k - 1])

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines of input. The first line contains two integers `n` and `k`, and the second line contains `n` integers. The function then determines the number of integers in the list that are less than or equal to the `k`-th integer, and prints the maximum of this count minus one and the count of integers that are less than or equal to the `k`-th integer, including the possibility of swapping the `k`-th integer with the next integer in the list. If the number of integers less than or equal to the `k`-th integer is greater than or equal to `k`, the function prints this count minus one. The function processes multiple test cases and prints the result for each case.

