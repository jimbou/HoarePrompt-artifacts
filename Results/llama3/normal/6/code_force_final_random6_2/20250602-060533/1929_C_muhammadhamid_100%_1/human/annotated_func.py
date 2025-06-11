#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three space-separated integers: k, x, and a. k is an integer between 2 and 30 (inclusive), x is an integer between 1 and 100 (inclusive), and a is an integer between 1 and 10^9 (inclusive).
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 1
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('Yes' if a >= s else 'No')
        
    #State: k is an integer, x is an integer, a is an integer, s is x + x * s // (k - 1), stdin contains no test cases, i is x - 1, and 'Yes' is printed if a is greater than or equal to s, otherwise 'No' is printed.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case contains three integers: k, x, and a. It calculates a value s based on k and x, and then prints 'Yes' if a is greater than or equal to s, otherwise it prints 'No'. The function continues processing test cases until all input has been consumed.

