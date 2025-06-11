#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing three integers a, b, m (1 <= a, b, m <= 10^18).
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        mn = min(a, b) + m
        
        if m % a == 0 and m % b == 0 and a != 1 and b != 1:
            print(mn // a + mn // b + 1)
        else:
            print(mn // a + mn // b)
        
    #State: t is an integer greater than or equal to 0, i is equal to t, stdin is empty, a is an integer between 1 and 10^18, b is an integer between 1 and 10^18, m is an integer between 1 and 10^18, mn is an integer equal to the minimum of a and b plus m. If m is divisible by both a and b, and both a and b are not equal to 1, then the program prints mn // a + mn // b + 1. Otherwise, the program prints the sum of the integer divisions of mn by a and mn by b.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers a, b, and m. It calculates the minimum of a and b plus m, and then prints the sum of the integer divisions of this result by a and b. If m is divisible by both a and b, and both a and b are not equal to 1, it adds 1 to the result before printing. The function processes all test cases and prints the results, leaving the standard input empty.

