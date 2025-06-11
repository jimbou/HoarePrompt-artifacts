#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing four integers p_i (0 <= p_i <= 200).
    print('\n'.join([str(sum(3 * (x // 2) + x % 2 * (i < 3) for i, x in
    enumerate(map(int, input().split()))) // 3) for _ in range(int(input()))]))
    #This is printed: The results of the calculations for each test case, one per line, where each result is the sum of the calculated values for each integer in the input, divided by 3, converted to a string.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of four integers. It calculates a value for each integer based on a specific formula, sums these values, and then divides the sum by 3. The results for each test case are printed to standard output, one result per line.

