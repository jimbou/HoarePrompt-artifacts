#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing three integers a, b, and m (1 <= a, b, m <= 10^18).
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        mn = min(a, b) + m
        
        if m % a == 0 and m % b == 0 and a != 1 and b != 1:
            print(mn // a + mn // b + 1)
        else:
            print(mn // a + mn // b)
        
    #State: The output will be t lines, each containing an integer that represents the minimum number of operations required to make a and b equal to their respective minimum values, considering the given conditions.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each case consists of three integers a, b, and m. It calculates and prints the minimum number of operations required to make a and b equal to their respective minimum values, considering the given conditions. The function handles cases where m is divisible by both a and b, as well as cases where it is not. The output is a series of integers, each representing the minimum number of operations required for the corresponding test case.

