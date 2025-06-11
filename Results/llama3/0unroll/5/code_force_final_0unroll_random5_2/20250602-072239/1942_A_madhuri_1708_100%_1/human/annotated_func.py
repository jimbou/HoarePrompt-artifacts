#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 10^3) and then t pairs of integers n and k (1 <= k <= n <= 10^3).
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        if k >= 2:
            if n == k:
                print(*[k for j in range(k)])
            else:
                print('-1')
        else:
            print(*[(j + 1) for j in range(n)])
        
    #State: The output state contains t number of lines. Each line contains either a sequence of integers or -1. If k is 1, the line contains a sequence of integers from 1 to n. If k is greater than 1, the line contains either a sequence of k repeated k times if n is equal to k, or -1 if n is greater than k.

#Overall this is what the function does:This function reads input from stdin, expecting an integer t followed by t pairs of integers n and k. It then generates and prints t lines of output. If k is 1, the function prints a sequence of integers from 1 to n. If k is greater than 1, it prints either a sequence of k repeated k times if n equals k, or -1 if n is greater than k.

