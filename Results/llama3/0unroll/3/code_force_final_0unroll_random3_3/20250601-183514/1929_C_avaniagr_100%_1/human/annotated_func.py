#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers k, x, and a, where k is an integer between 2 and 30 (inclusive), x is an integer between 1 and 100 (inclusive), and a is an integer between 1 and 10^9 (inclusive).
    for s in [*open(0)][1:]:
        k, x, a = map(int, s.split())
        
        if x < k - 1:
            if a >= x + 1:
                print('YES')
            else:
                print('NO')
        elif x == k - 1:
            if a >= x + 2:
                print('YES')
            else:
                print('NO')
        else:
            z = k - 2
            for i in range(x - k + 3):
                z += z // (k - 1) + 1
            if a >= z:
                print('YES')
            else:
                print('NO')
        
    #State: The output state will be a series of 'YES' or 'NO' printed to the console, each corresponding to a test case in the input. The output will indicate whether the value of 'a' is sufficient to meet the conditions specified in the loop, based on the values of 'k' and 'x'.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains three integers: k, x, and a. It then evaluates whether the value of 'a' is sufficient based on the values of 'k' and 'x', and prints 'YES' or 'NO' to the console for each test case, indicating whether the condition is met. The condition is met if 'a' is greater than or equal to a calculated value that depends on 'k' and 'x'. The function handles three cases: when 'x' is less than 'k-1', when 'x' is equal to 'k-1', and when 'x' is greater than or equal to 'k-1'.

