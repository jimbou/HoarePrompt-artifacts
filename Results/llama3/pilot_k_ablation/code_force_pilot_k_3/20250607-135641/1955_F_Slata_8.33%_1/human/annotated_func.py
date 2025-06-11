#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing four integers p_i (0 <= p_i <= 200).
    for i in range(int(input())):
        a, b, c, d = map(int, input().split())
        
        print(a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 3 == 3))
        
    #State: `a`, `b`, `c`, `d` are integers between 0 and 200, the sum of the integer divisions of `a`, `b`, `c`, and `d` by 2, plus the integer value of the expression `a % 2 + b % 2 + c % 3 == 3` has been printed `t` times, `i` is `t`, stdin is empty, and int(input()) is 0.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of four integers between 0 and 200. For each test case, it calculates and prints the sum of the integer divisions of the four integers by 2, plus 1 if the sum of the remainders of the first three integers divided by 2 and the fourth integer divided by 3 is equal to 3. The function repeats this process for a number of test cases specified by the first integer read from standard input.

