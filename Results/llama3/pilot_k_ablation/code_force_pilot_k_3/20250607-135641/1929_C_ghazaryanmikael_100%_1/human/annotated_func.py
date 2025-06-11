#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t sets of three space-separated integers k, x, and a (2 <= k <= 30, 1 <= x <= 100, 1 <= a <= 10^9).
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 1
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('YES' if a >= s else 'NO')
        
    #State: k is an integer between 2 and 30, x is at least 1, a is an integer between 1 and 10^9, s is at least x + 1, _ is t-1, i is x-1, and the string 'YES' is printed if a is greater than or equal to s, otherwise the string 'NO' is printed, stdin is empty, and int(input()) is 0.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers: k, x, and a. It calculates a value s based on k and x, and then prints 'YES' if a is greater than or equal to s, otherwise it prints 'NO'. The function processes all test cases and then terminates, leaving the standard input empty.

