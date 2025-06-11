#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then for each test case, two integers (n and k) separated by a space. 1 <= k <= n <= 10^3.
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        if k >= 2:
            if n == k:
                print(*[k for j in range(k)])
            else:
                print('-1')
        else:
            print(*[j for j in range(n)])
        
    #State: `open(0)` is a file object with at least `t+1` lines, where `t` is the number of test cases, `s` is the last line of the file, `n` is an integer equal to the first integer in the last line of the file, `k` is an integer equal to the second integer in the last line of the file. If `k` is greater than or equal to 2, then if `n` is equal to `k`, a list of `k` number of `k` is being printed. Otherwise, -1 is being printed. If `k` is less than 2, a list of integers from 0 to `n-1` is being printed.

#Overall this is what the function does:This function reads input from standard input, where the first line contains the number of test cases, and each subsequent line contains two integers, n and k. It then processes each test case based on the value of k. If k is greater than or equal to 2, it checks if n is equal to k. If they are equal, it prints a list of k repeated k times. Otherwise, it prints -1. If k is less than 2, it prints a list of integers from 0 to n-1. The function does not return any value but prints the results for each test case.

