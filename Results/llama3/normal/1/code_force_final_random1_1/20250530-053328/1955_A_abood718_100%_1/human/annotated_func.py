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
        
    #State: `i` is t-1, stdin is empty, and no more output is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each case consists of three integers: n, a, and b. For each case, it calculates and prints the maximum number of items that can be purchased with a and b, considering the constraints that a and b are limited to 30 and n is limited to 100. The function handles three scenarios: when 2a is less than b, when n is even, and when n is odd. After processing all test cases, the function leaves the input stream empty and does not produce any further output.

