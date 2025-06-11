#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing four integers p_i (0 <= p_i <= 200).
    for i in range(int(input())):
        a, b, c, d = map(int, input().split())
        
        print(a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 2 == 3))
        
    #State: `a`, `b`, `c`, and `d` are integers between 0 and 200, stdin contains an integer 0 (0 <= 0 <= 10^4) followed by 0 lines, each containing four integers p_i (0 <= p_i <= 200), and the sum of the integer division of `a`, `b`, `c`, and `d` by 2 plus 1 if the sum of the remainder of `a`, `b`, `c`, and `d` divided by 2 is equal to 3 is being printed

#Overall this is what the function does:The function reads a series of lines from standard input, where each line contains four integers between 0 and 200. For each line, it calculates the sum of the integer division of these integers by 2, and adds 1 if the sum of the remainders of these integers divided by 2 is equal to 3. The function then prints this calculated sum for each line. After processing all lines, the function leaves the standard input empty.

