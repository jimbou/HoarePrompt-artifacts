#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 10^3) followed by t lines, each containing two integers x (1 ≤ x ≤ 10^8) and n (1 ≤ n ≤ x).
    x, n = list(map(int, input().split()))
    ans = 0
    for i in range(1, isqrt(x) + 1):
        if x % i == 0:
            if n <= x // i:
                ans = max(ans, i)
            elif n <= i:
                ans = max(ans, x // i)
        
    #State: ans is the largest divisor of x that is less than or equal to n, x remains unchanged, n remains unchanged, stdin remains unchanged.
    print(ans)
    #This is printed: the largest divisor of x that is less than or equal to n

#Overall this is what the function does:The function reads two integers x and n from standard input, finds the largest divisor of x that is less than or equal to n, and prints this value. The function does not modify the input values x and n, and it does not consume any additional input from standard input beyond the initial two integers. The function's output is a single integer, which is the largest divisor of x that is less than or equal to n.

