#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two positive integers n and m, such that 1 <= n, m <= 2 * 10^6.
    t = int(input())
    for T in range(t):
        [n, m] = input().split()
        
        [n, m] = [int(n), int(m)]
        
        ans = 0
        
        for b in range(1, min(n, m) + 1):
            ans = ans + n // b + 1
        
        print(ans)
        
    #State: t is a positive integer greater than or equal to 0, T is t, stdin contains no test cases, n is an integer, m is an integer, ans is the sum of n divided by all integers from 1 to min(n, m) plus min(n, m), b is min(n, m), min(n, m) is greater than or equal to 1, and the sum of n divided by all integers from 1 to min(n, m) plus min(n, m) is being printed

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two positive integers n and m. It calculates the sum of n divided by all integers from 1 to the minimum of n and m, plus the minimum of n and m, and prints this sum for each test case. The function processes all test cases and then terminates, leaving the standard input empty.

