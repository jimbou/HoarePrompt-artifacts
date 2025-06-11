#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t sets of three integers a, b, m (1 <= a, b, m <= 10^18).
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        mn = min(a, b) + m
        
        if m % a == 0 and m % b == 0 and a != 1 and b != 1:
            print(mn // a + mn // b + 1)
        else:
            print(mn // a + mn // b)
        
    #State: t is an integer between 0 and 10^4 inclusive, i is t, a is an integer, b is an integer, m is an integer, mn is an integer equal to the minimum of a and b plus m. If m is divisible by both a and b, and both a and b are not equal to 1, then the expression mn // a + mn // b + 1 is printed. Otherwise, the sum of the integer division of mn by a and the integer division of mn by b is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers a, b, and m. It calculates the minimum of a and b plus m, and then prints the sum of the integer divisions of this minimum value by a and b. If m is divisible by both a and b, and both a and b are not equal to 1, it adds 1 to the result before printing. The function processes all test cases and prints the results accordingly.

