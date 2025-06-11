#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing three integers a, b, and m (1 <= a, b, m <= 10^18).
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        mn = min(a, b) + m
        
        if m % a == 0 and m % b == 0 and a != 1 and b != 1:
            print(mn // a + mn // b + 1)
        else:
            print(mn // a + mn // b)
        
    #State: The output state will contain t lines, each containing a single integer. The integer on each line will be the result of the calculation mn // a + mn // b + 1 if m is divisible by both a and b and a and b are not equal to 1, otherwise it will be mn // a + mn // b.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers a, b, and m. It then calculates and prints the result of the expression mn // a + mn // b, where mn is the minimum of a and b plus m. If m is divisible by both a and b and neither a nor b is 1, it adds 1 to the result. The function outputs the calculated results for each test case, one per line.

