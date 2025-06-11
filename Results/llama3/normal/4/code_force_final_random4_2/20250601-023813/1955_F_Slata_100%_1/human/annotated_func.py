#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing four integers p_i (0 <= p_i <= 200).
    for i in range(int(input())):
        a, b, c, d = map(int, input().split())
        
        print(a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 2 == 3))
        
    #State: `a`, `b`, `c`, and `d` are integers, `i` is equal to the initial value of `t`, stdin is empty, and this is printed: the sum of the integer divisions of `a`, `b`, `c`, and `d` by 2, plus 1 if the sum of the remainders of `a`, `b`, and `c` divided by 2 equals 3, otherwise 0

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of four integers. For each test case, it calculates and prints the sum of the integer divisions of the four numbers by 2, plus 1 if the sum of the remainders of three of the numbers divided by 2 equals 3, otherwise 0. The function processes all test cases and then terminates, leaving the standard input empty.

