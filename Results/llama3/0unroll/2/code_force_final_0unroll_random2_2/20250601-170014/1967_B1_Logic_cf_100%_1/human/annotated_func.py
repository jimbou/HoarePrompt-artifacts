#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two positive integers n and m, where 1 <= n, m <= 2 * 10^6.
    t = int(input())
    for T in range(t):
        [n, m] = input().split()
        
        [n, m] = [int(n), int(m)]
        
        ans = n
        
        for b in range(2, min(n, m) + 1):
            ans = ans + (n + b) // (b * b)
        
        print(ans)
        
    #State: The output state after the loop executes all the iterations is that the variable `ans` will hold the value of the sum of `n` and the sum of the integer divisions of `n + b` by `b * b` for all `b` from 2 to the minimum of `n` and `m` (inclusive), and this value will be printed to the console for each test case. The variable `t` will remain unchanged, and the stdin will be empty after all test cases have been processed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains two positive integers n and m. For each test case, it calculates the sum of n and the sum of the integer divisions of n + b by b * b for all b from 2 to the minimum of n and m (inclusive), and prints this value to the console. The function processes all test cases and empties the standard input.

