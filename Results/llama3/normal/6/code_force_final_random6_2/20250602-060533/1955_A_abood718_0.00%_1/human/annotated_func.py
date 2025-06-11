#State of the program right berfore the function call: stdin contains t+1 inputs: first an integer t (1 <= t <= 10^4), then t sets of three integers n, a, and b (1 <= n <= 100, 1 <= a, b <= 30).
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
        
    #State: `i` is `t`, `A`, `B`, `C` are integers where `A` is equal to `n` (1 <= n <= 100), `B` and `C` are integers where `B` and `C` are not assigned any value yet, stdin is empty. If `B` is less than half of `C`, the product of `A` and `B` is printed. If `B` is either less than or equal to half of `C`, then if `A` is even, the integer division of the product of `A` and `C` by 2 is printed. If `A` is odd, the integer part of `A/2` is printed, and `X` * `C` + `B` is printed, where `X` is the integer part of `A/2` and `B` is either less than or equal to half of `C`.

#Overall this is what the function does:This function reads a series of inputs from stdin, where each set of inputs contains three integers: n, a, and b. It then performs calculations based on the values of a and b, and prints the results. If a is less than half of b, it prints the product of n and a. If a is less than or equal to half of b, it checks if n is even. If n is even, it prints the integer division of the product of n and b by 2. If n is odd, it prints the integer part of n/2 and then prints the product of this value and b, plus a. The function continues this process until all input sets have been processed, at which point stdin is empty.

