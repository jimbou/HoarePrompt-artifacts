#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two positive integers n and m, where 1 <= n, m <= 2 * 10^6.
    t = int(input())
    for T in range(t):
        [n, m] = input().split()
        
        [n, m] = [int(n), int(m)]
        
        ans = n
        
        for b in range(2, min(n, m) + 1):
            ans = ans + (n + b) // (b * b)
        
        print(ans)
        
    #State: The value of `ans` is printed to the console for each test case, and the value of `t` remains unchanged. The stdin is empty after all test cases have been processed.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case contains two positive integers n and m. It calculates a value 'ans' for each test case, which is the sum of n and the number of multiples of each number b (2 <= b <= min(n, m)) that are less than or equal to n. The calculated 'ans' value is then printed to the console for each test case. After processing all test cases, the function leaves the standard input empty.

