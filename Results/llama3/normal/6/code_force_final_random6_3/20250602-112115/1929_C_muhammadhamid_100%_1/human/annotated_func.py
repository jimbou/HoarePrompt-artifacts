#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t sets of three space-separated integers k, x, and a (2 <= k <= 30, 1 <= x <= 100, 1 <= a <= 10^9).
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 1
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('Yes' if a >= s else 'No')
        
    #State: k is an integer between 2 and 30, x is an integer greater than or equal to 0, a is an integer between 1 and 10^9, s is an integer greater than 1 and is equal to s + (x - 1) * (s // (k - 1) + 1), stdin is empty, _ is t-1, i is x - 1, and 'Yes' is printed if a is greater than or equal to s otherwise 'No' is printed.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each case consists of three integers: k, x, and a. It calculates a value s based on k and x, and then prints 'Yes' if a is greater than or equal to s, otherwise it prints 'No'. The function processes all test cases and empties the standard input.

