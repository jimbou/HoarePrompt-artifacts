#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: two integers x and n, where x and n are positive integers and n is less than or equal to x.
    x, n = list(map(int, input().split()))
    ans = 0
    for i in range(1, isqrt(x) + 1):
        if x % i == 0:
            if n <= x // i:
                ans = max(ans, i)
            elif n <= i:
                ans = max(ans, x // i)
        
    #State: `x` is a positive integer, `n` is a positive integer less than or equal to `x`, `stdin` contains multiple test cases minus one, `i` is equal to the square root of `x` plus one, `ans` is the maximum divisor of `x` that is less than or equal to `n`.
    print(ans)
    #This is printed: the maximum divisor of x that is less than or equal to n

#Overall this is what the function does:The function reads two positive integers x and n from standard input, where n is less than or equal to x, and prints the maximum divisor of x that is less than or equal to n.

