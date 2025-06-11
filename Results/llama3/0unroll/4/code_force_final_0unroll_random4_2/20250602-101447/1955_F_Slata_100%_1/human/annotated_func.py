#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing four integers p_i (0 <= p_i <= 200).
    for i in range(int(input())):
        a, b, c, d = map(int, input().split())
        
        print(a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 2 == 3))
        
    #State: The output will be the sum of the integer divisions of the input integers by 2, plus 1 if the sum of the remainders of the integer divisions of three of the input integers by 2 is equal to 3. This will be repeated for each line of input.

#Overall this is what the function does:This function reads a series of lines from standard input, where each line contains four integers. It calculates the sum of the integer divisions of these integers by 2, and adds 1 if the sum of the remainders of three of the integer divisions by 2 equals 3. This calculation is performed for each line of input, and the results are printed to standard output.

