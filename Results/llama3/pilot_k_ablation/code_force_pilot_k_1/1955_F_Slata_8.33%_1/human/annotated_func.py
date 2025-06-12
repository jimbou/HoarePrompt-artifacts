#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing four integers p_i (0 <= p_i <= 200).
    for i in range(int(input())):
        a, b, c, d = map(int, input().split())
        
        print(a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 3 == 3))
        
    #State: `i` is equal to the initial value of `t`, stdin is empty, `a`, `b`, `c`, `d` are the last four integers in the input (0 <= a, b, c, d <= 200), and the loop has printed the sum of the integer divisions of `a`, `b`, `c`, and `d` by 2, plus the integer value of the sum of the remainders of `a`, `b`, and `c` divided by 3, which is equal to 3, for each of the `t` lines in the input.

#Overall this is what the function does:This function reads a series of lines from standard input, where each line contains four integers. It then calculates and prints the sum of the integer divisions of these four integers by 2, plus the integer value of the sum of the remainders of the first three integers divided by 3, which is equal to 3, for each line. The function processes a number of lines specified by the first integer read from standard input.

