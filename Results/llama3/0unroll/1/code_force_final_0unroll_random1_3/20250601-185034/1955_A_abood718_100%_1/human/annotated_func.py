#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing three integers n, a, and b (1 <= n <= 100, 1 <= a, b <= 30).
    for i in range(int(input())):
        A, B, C = map(int, input().split())
        
        if B * 2 < C:
            print(A * B)
        elif A % 2 == 0:
            print(int(A * C / 2))
        else:
            X = A // 2
            print(X * C + B)
        
    #State: The output will be the result of the calculations for each test case, which will be the maximum number of candies that can be put in a bag for each test case.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers: n, a, and b. It then calculates and prints the maximum number of candies that can be put in a bag for each test case, based on the given values of a and b, and whether n is even or odd. The function processes all test cases and outputs the results, one per line.

