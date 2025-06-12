#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 10^3) and then t pairs of integers n and k (1 <= k <= n <= 10^3).
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        if k >= 2:
            if n == k:
                print(*[k for j in range(k)])
            else:
                print('-1')
        else:
            print(*[j for j in range(n)])
        
    #State: stdin is empty, `n` and `k` are the last pair of integers read from stdin, and the file object is closed. If `k` is greater than or equal to 2 for all pairs, then if `n` equals `k` for all pairs, a list of `n` elements, each equal to `n`, is printed for each pair; otherwise, -1 is printed for each pair. If `k` is less than 2 for any pair, a list of integers from 0 to `n-1` is printed for that pair.

#Overall this is what the function does:The function reads pairs of integers (n, k) from standard input, where 1 <= k <= n <= 10^3, and prints a list of integers for each pair. If k is greater than or equal to 2, it prints a list of n elements, each equal to n, if n equals k; otherwise, it prints -1. If k is less than 2, it prints a list of integers from 0 to n-1. The function continues this process until all pairs have been read from standard input, at which point the file object is closed and standard input is empty.

