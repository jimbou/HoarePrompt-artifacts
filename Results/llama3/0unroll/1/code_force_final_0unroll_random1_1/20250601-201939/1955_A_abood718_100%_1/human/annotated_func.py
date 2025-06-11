#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains one integer t (1 <= t <= 10^4). Each of the following t lines contains three integers n, a, and b (1 <= n <= 100, 1 <= a, b <= 30).
    for i in range(int(input())):
        A, B, C = map(int, input().split())
        
        if B * 2 < C:
            print(A * B)
        elif A % 2 == 0:
            print(int(A * C / 2))
        else:
            X = A // 2
            print(X * C + B)
        
    #State: The output state will contain 't' number of lines, each containing the calculated result based on the given conditions for each test case.

#Overall this is what the function does:This function reads multiple lines of input from stdin, where the first line contains an integer t, representing the number of test cases. For each test case, it reads three integers n, a, and b, and calculates a result based on the given conditions. If 2a is less than b, it prints the product of n and a. If n is even, it prints the product of n and b divided by 2. Otherwise, it prints the product of n divided by 2, rounded down, multiplied by b, plus a. The function outputs 't' number of lines, each containing the calculated result for each test case.

