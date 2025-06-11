#State of the program right berfore the function call: stdin contains t+1 inputs: the first input is a positive integer t (1 <= t <= 10^4) and the rest t inputs are three space-separated positive integers n, a, and b (1 <= n <= 100, 1 <= a, b <= 30).
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        if n % 2:
            if 2 * a < b:
                print(a * n)
            else:
                print(n // 2 * b + a)
        elif 2 * a < b:
            print(a * n)
        else:
            print(n // 2 * b)
        
    #State: `_` is `t`, stdin contains no inputs. If `n` is odd and `2 * a` is less than `b`, the product of `a` and `n` is printed. If `n` is odd and `2 * a` is not less than `b`, the value of the expression `n // 2 * b + a` is printed. If `n` is even and `2a` is less than `b`, the product of `a` and `n` is printed. If `n` is even and `2a` is not less than `b`, `n * b / 2` is printed.

#Overall this is what the function does:This function reads a series of inputs from stdin, where each input consists of three positive integers n, a, and b. It then prints the result of a calculation based on the values of n, a, and b. If n is odd and 2a is less than b, it prints the product of a and n. If n is odd and 2a is not less than b, it prints the value of the expression n // 2 * b + a. If n is even and 2a is less than b, it prints the product of a and n. If n is even and 2a is not less than b, it prints n * b / 2. The function repeats this process for a number of iterations specified by the first input, and then terminates, leaving stdin empty.

