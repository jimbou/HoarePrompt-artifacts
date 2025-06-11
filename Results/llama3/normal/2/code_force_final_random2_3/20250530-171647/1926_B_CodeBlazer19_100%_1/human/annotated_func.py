#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t test cases. Each test case consists of an integer n (2 <= n <= 10) followed by n lines, each containing a string of n characters '0' or '1'.
    t = int(input())
    for i in range(t):
        n = int(input())
        
        a = 0
        
        b = ''
        
        for j in range(n):
            s = input()
            if s.count('1') == 1:
                a = 'TRIANGLE'
            elif s.count('1') > 1:
                b = 'SQUARE'
        
        if a != 0:
            print(a)
        else:
            print(b)
        
    #State: t is an integer between 1 and 100 (inclusive) and is equal to 0, i is t-1, n is an integer and is at least n, j is n, s is a string containing the input from stdin, and stdin contains 0 test cases. If a is not 0, then based on the test cases in s, either 'TRIANGLE' or 0 is printed as the value of a, and b is either 'SQUARE' or an empty string if any test case contains exactly one '1', or 'SQUARE' if any test case contains more than one '1'. If a is 0, then the value of b is printed.

#Overall this is what the function does:This function reads input from stdin, processes a series of test cases, and prints the shape type ('TRIANGLE' or 'SQUARE') based on the input strings. It iterates through each test case, checks the number of '1's in each string, and determines the shape type accordingly. If a 'TRIANGLE' is found, it is printed; otherwise, if a 'SQUARE' is found, it is printed. The function processes all test cases and prints the corresponding shape types.

