#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing four integers p_i (0 <= p_i <= 200).
    for i in range(int(input())):
        a, b, c, d = map(int, input().split())
        
        print(a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 3 == 3))
        
    #State: The output will be the sum of the integer divisions of the four input integers by 2, plus 1 if the sum of the remainders of the first three integers divided by 3 is equal to 3, for each test case.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each case consists of four integers. For each test case, it calculates and prints the sum of the integer divisions of the four input integers by 2, plus 1 if the sum of the remainders of the first three integers divided by 3 is equal to 3. The function processes all test cases and produces the corresponding output for each case.

