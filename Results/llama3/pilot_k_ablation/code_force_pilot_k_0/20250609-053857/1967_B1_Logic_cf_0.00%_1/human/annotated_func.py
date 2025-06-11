#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains the number of test cases t (1 <= t <= 10^4). Each test case contains two positive integers n and m (1 <= n, m <= 2 * 10^6).
    t = int(input())
    for T in range(t):
        [n, m] = input().split()
        
        [n, m] = [int(n), int(m)]
        
        ans = 0
        
        for b in range(1, min(n, m) + 1):
            ans = ans + n // b + 1
        
        print(ans)
        
    #State: The output state after the loop executes all the iterations is a series of integers, each representing the sum of the number of multiples of each number from 1 to the minimum of `n` and `m` (inclusive), plus 1, for each test case. The value of `t` remains unchanged, and the input from stdin is consumed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two positive integers n and m. For each test case, it calculates the sum of the number of multiples of each number from 1 to the minimum of n and m (inclusive), plus 1, and prints the result. The function consumes the input from stdin and produces a series of integers as output, one for each test case.

