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
        
    #State: The loop has executed for the number of times specified by the integer `t` read from `stdin`. The values of `A`, `B`, and `C` are the last set of three integers read from `stdin`. If `B * 2 < C`, the product of `A` and `B` is printed. Otherwise, if `A` is even, the integer part of the product of `A` and `C` divided by 2 is printed. If `A` is odd, half of `A` is calculated and stored in `X`, and then `X * C + B` is printed.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each case consists of three integers: A, B, and C. For each case, it calculates and prints a value based on the following rules: if B is less than half of C, it prints the product of A and B; if A is even, it prints the integer part of the product of A and C divided by 2; if A is odd, it calculates half of A, prints it, and then prints the product of the half and C plus B. The function repeats this process for the number of test cases specified by the first integer read from standard input.

