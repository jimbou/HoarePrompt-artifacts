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
        
    #State: `i` is `t`, `A`, `B`, `C` are integers where `A` is greater than or equal to 1 and less than or equal to 100, `B` and `C` are greater than or equal to 1 and less than or equal to 30, stdin is empty. If `B` is less than half of `C`, the product of `A` and `B` is printed. If `B` is greater than or equal to half of `C`, then if `A` is even, the integer part of half of the product of `A` and `C` is printed. If `A` is odd, an integer `X` between 0 and 49 is used to calculate and print the value of `X` * `C` + `B`.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers A, B, and C. It then prints a calculated value for each test case based on the following rules: if B is less than half of C, it prints the product of A and B; if B is greater than or equal to half of C, it prints the integer part of half of the product of A and C if A is even, or the value of X * C + B if A is odd, where X is the integer part of A divided by 2. The function continues this process until all test cases have been read from standard input, at which point the input is empty.

