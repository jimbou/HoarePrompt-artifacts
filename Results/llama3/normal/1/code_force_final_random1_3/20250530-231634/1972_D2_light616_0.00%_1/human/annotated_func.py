#State of the program right berfore the function call: n and m are positive integers.
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
        
    #State: n is greater than or equal to 144, m is greater than or equal to 144, x is 13, y is 12, cnt is increased by at least 1 plus the minimum of n / ((3 + 1) * 3), m // ((3 + 1) * 1), n / ((3 + 3) * 3), m // ((3 + 3) * 2), n / 36, m / 36, n / 48, m / 48, n / 60, m / 60, n / 72, m / 72, n / 84, m / 84, n / 96, m / 96, n / 108, m / 108, n / 120, m / 120, n / 132, m / 132, n / 144, m / 144.
    print(cnt)
    #This is printed: cnt (where cnt is increased by at least 1 plus the minimum of n / ((3 + 1) * 3), m // ((3 + 1) * 1), n / ((3 + 3) * 3), m // ((3 + 3) * 2), n / 36, m / 36, n / 48, m / 48, n / 60, m / 60, n / 72, m / 72, n / 84, m / 84, n / 96, m / 96, n / 108, m / 108, n / 120, m / 120, n / 132, m / 132, n / 144, m / 144)

#Overall this is what the function does:Calculates and prints the count of pairs of coprime numbers (x, y) such that (x + y) * x <= n and (x + y) * y <= m, where n and m are positive integers. The function takes no parameters and returns the count of such pairs.

#State of the program right berfore the function call: stdin contains one input: an integer t (1 ≤ t ≤ 10^4)
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` is at least `t`, stdin contains no input, and the function `func_1()` has been executed `t` times.

#Overall this is what the function does:Reads an integer `t` from standard input and executes the function `func_1()` `t` times, leaving the standard input empty.

