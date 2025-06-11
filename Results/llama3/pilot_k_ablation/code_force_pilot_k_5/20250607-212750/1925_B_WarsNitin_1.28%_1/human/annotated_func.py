#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers x (1 <= x <= 10^8) and n (1 <= n <= x).
    for q in range(int(input())):
        x, n = list(map(int, input().split(' ')))
        
        ans = 1
        
        for i in range(1, int(sqrt(x)) + 1):
            if x % i == 0:
                if x - n * i >= 0 and (x - n * i) % i == 0:
                    ans = max(ans, i)
                if x - n * (x // i) >= 0 and x // i > 0 and x - n * (x // i) % (x // i
                    ) == 0:
                    ans = max(ans, x // i)
        
        print(ans)
        
    #State: `q` is `int(input()) - 1`, `ans` is the maximum divisor `i` of `x` such that `x - n * i` is non-negative and divisible by `i`, or `x - n * (x // i)` is non-negative, `x // i` is positive, and `x - n * (x // i)` is divisible by `x // i`, `x` is an integer between 1 and 10^8, `n` is an integer between 1 and `x`, `i` is the square root of `x` plus 1, `int(input())` is greater than or equal to 0, and `ans` is printed, `stdin` is empty.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two integers x and n. It then finds the maximum divisor i of x such that x - n * i is non-negative and divisible by i, or x - n * (x // i) is non-negative, x // i is positive, and x - n * (x // i) is divisible by x // i. The function prints the maximum divisor for each test case.

