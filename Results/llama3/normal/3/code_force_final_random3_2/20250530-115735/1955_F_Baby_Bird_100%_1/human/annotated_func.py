#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing four integers p_i (0 <= p_i <= 200).
    print('\n'.join([str(sum(3 * (x // 2) + x % 2 * (i < 3) for i, x in
    enumerate(map(int, input().split()))) // 3) for _ in range(int(input()))]))
    #This is printed: The results of the calculations for each test case, separated by newline characters, where each result is the sum of the calculated values for the four integers in each test case, divided by 3

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of four integers. It calculates a value for each test case by summing the results of a specific calculation involving the four integers, and then prints the result of this calculation divided by 3, one result per line. The function processes multiple test cases, as specified by an initial integer input indicating the number of test cases to follow.

