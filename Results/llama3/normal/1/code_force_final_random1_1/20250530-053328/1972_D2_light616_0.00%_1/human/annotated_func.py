#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6.
    x = 1
    cnt = 0
    n, m = map(int, input().split())
    while x * x <= n:
        y = 1
        
        while (x + y) * x <= n and (x + y) * y <= m:
            if math.gcd(x, y) == 1:
                cnt += min(n / ((x + y) * x), m // ((x + y) * y))
            y += 1
        
        x += 1
        
    #State: cnt is increased by the sum of min(n / k, m // (k * (k - 1))) for all positive integers k such that k is less than or equal to the minimum of the square root of n and the square root of m, and k is relatively prime to k - 1, and x is increased to the minimum of the square root of n and the square root of m plus 1.
    print(cnt)
    #This is printed: cnt (where cnt is the sum of min(n / k, m // (k * (k - 1))) for all positive integers k such that k is less than or equal to the minimum of the square root of n and the square root of m, and k is relatively prime to k - 1)

#Overall this is what the function does:Calculates and prints the sum of minimum values between n/k and m/(k*(k-1)) for all positive integers k less than or equal to the minimum of the square roots of n and m, where k is relatively prime to k-1, given two positive integers n and m as input.

#State of the program right berfore the function call: stdin contains one input: an integer t (1 <= t <= 10^4)
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` is an integer greater than or equal to 0 and less than or equal to 10^4 (inclusive), `_` is `t-1`, stdin is empty, and the function `func_1()` has been executed `t` times.

#Overall this is what the function does:Reads an integer from standard input and executes the function `func_1()` that many times.

