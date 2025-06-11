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
        
    #State: `i` is `t-1`, `A`, `B`, `C` are integers that are assigned the last three integers from the input, stdin contains an empty string. If `B * 2` is less than `C`, the product of `A` and `B` is printed. If `B * 2` is not less than `C`, then if `A` is even, the integer part of the product of `A` and `C` divided by 2 is printed. If `A` is odd, the value of `X` which is equal to (`A` - 1) / 2 is printed, and the value of `X * C + B` is printed.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each case consists of three integers: n, a, and b. For each case, it calculates and prints a value based on the following conditions: if b is less than half of c, it prints the product of n and b; if n is even, it prints the integer part of the product of n and c divided by 2; if n is odd, it prints the value of (n-1)/2 and then the product of this value and c plus b. The function processes all test cases and then terminates, leaving the input stream empty.

