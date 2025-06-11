#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing four integers p_i (0 <= p_i <= 200).
    for i in range(int(input())):
        a, b, c, d = map(int, input().split())
        
        print(a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 2 == 3))
        
    #State: The output will be the sum of the integer divisions of a, b, c, and d by 2, plus 1 if the sum of the remainders of a, b, and c divided by 2 is 3, for each of the t lines.

#Overall this is what the function does:The function reads a series of lines from standard input, where each line contains four integers. It then calculates and prints the sum of the integer divisions of these four integers by 2, plus 1 if the sum of the remainders of the first three integers divided by 2 is 3. This calculation is performed for each line of input, and the results are printed to standard output.

