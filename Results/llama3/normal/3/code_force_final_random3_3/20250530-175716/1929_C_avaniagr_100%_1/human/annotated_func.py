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
        
    #State: The loop has executed for all lines in the input, and for each line, 'YES' or 'NO' has been printed depending on the values of k, x, and a. The loop has finished executing, and the program has terminated.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains three integers k, x, and a. For each test case, it determines whether a certain condition is met based on the values of k, x, and a, and prints 'YES' if the condition is met or 'NO' otherwise. The function processes all test cases in the input and terminates after printing the results for all cases.

