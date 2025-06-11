#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing four integers p_i (0 <= p_i <= 200).
    for i in range(int(input())):
        a, b, c, d = map(int, input().split())
        
        print(a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 3 == 3))
        
    #State: `a`, `b`, `c`, `d` are integers (0 <= `a`, `b`, `c`, `d` <= 200), stdin contains 0 lines, each containing four integers p_i (0 <= p_i <= 200), t is an integer (1 <= t <= 10^4) and t is decreased by t, and this is printed: the sum of the integer divisions of `a`, `b`, `c`, and `d` by 2, plus the integer value of the sum of the remainders of `a`, `b`, and `c` divided by 3, which is equal to 3

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of four integers. For each test case, it calculates and prints the sum of the integer divisions of the four numbers by 2, plus the integer value of the sum of the remainders of the first three numbers divided by 3, which is equal to 3. The function processes all test cases and then terminates, leaving the standard input empty.

