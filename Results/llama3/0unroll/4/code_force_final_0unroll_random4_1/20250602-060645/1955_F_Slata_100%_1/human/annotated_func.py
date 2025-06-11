#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing four integers p_i (0 <= p_i <= 200).
    for i in range(int(input())):
        a, b, c, d = map(int, input().split())
        
        print(a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 2 == 3))
        
    #State: The output state will be the sum of the integer divisions of the input integers by 2, plus 1 if the sum of the remainders of the integer divisions of three of the input integers by 2 is 3. This will be repeated for each of the t lines of input.

#Overall this is what the function does:This function reads a series of lines from standard input, where each line contains four integers. It calculates and prints the sum of the integer divisions of these integers by 2, with an additional 1 added to the sum if the remainders of three of the integer divisions by 2 sum up to 3. This calculation is repeated for each line of input, with the results printed out one per line.

