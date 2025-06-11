#State of the program right berfore the function call: stdin contains t+1 inputs: first an integer t (1 <= t <= 10^4) and then t lines, each containing three integers n, a, and b (1 <= n <= 100, 1 <= a, b <= 30).
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
        
    #State: The output will contain t lines, each containing one or two integers. The first line will contain the result of A * B if B * 2 is less than C. If A is even, the first line will contain the result of A * C / 2. If A is odd, the first line will contain A // 2 and the second line will contain the result of (A // 2) * C + B.

#Overall this is what the function does:This function reads input from stdin, processes t sets of three integers (A, B, C), and prints the results of different calculations based on the values of A, B, and C. For each set, if B * 2 is less than C, it prints A * B. If A is even, it prints A * C / 2. If A is odd, it prints A // 2 on the first line and (A // 2) * C + B on the second line. The function generates t lines of output, with some lines containing one integer and others containing two integers.

