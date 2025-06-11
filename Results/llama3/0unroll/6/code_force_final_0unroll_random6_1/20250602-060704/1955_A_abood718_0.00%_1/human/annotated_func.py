#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing three integers n, a, and b (1 <= n <= 100, 1 <= a, b <= 30).
    for i in range(int(input())):
        A, B, C = map(int, input().split())
        
        if B * 2 < C:
            print(A * B)
        elif A % 2 == 0:
            print(int(A * C / 2))
        else:
            X = A // 2
            print(X)
            print(X * C + B)
        
    #State: The output state will contain t lines, each containing the result of the calculations performed inside the loop. The result will be either A * B, int(A * C / 2), or X (A // 2) followed by X * C + B, depending on the conditions met in each iteration.

#Overall this is what the function does:Calculates and prints the result of a series of mathematical operations based on input values A, B, and C, repeating the process for a specified number of test cases (t). For each test case, it either prints A * B, int(A * C / 2), or two values: A // 2 and (A // 2) * C + B, depending on the conditions met.

