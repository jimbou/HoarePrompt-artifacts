#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing four integers p_i (0 <= p_i <= 200).
    for i in range(int(input())):
        a, b, c, d = map(int, input().split())
        
        print(a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 2 == 3))
        
    #State: The loop has finished executing, and the output state is the sum of the integer divisions of `a`, `b`, `c`, `d` by 2 plus 1 if the sum of the remainders of `a`, `b`, `c`, `d` divided by 2 is equal to 3, printed for each iteration of the loop.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of four integers. For each test case, it calculates the sum of the integer divisions of the four numbers by 2, and adds 1 to the sum if the sum of the remainders of the four numbers divided by 2 is equal to 3. The function then prints the calculated sum for each test case.

