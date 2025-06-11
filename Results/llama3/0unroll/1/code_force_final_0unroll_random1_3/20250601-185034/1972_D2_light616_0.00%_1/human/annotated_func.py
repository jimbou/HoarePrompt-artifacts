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
        
    #State: cnt is the number of coprime pairs (a, b) such that 1 <= a <= n and 1 <= b <= m
    print(cnt)
    #This is printed: cnt (where cnt is the number of coprime pairs (a, b) such that 1 <= a <= n and 1 <= b <= m)

#Overall this is what the function does:Calculates and prints the number of coprime pairs (a, b) within the given ranges 1 <= a <= n and 1 <= b <= m, where n and m are positive integers provided as input.

#State of the program right berfore the function call: stdin contains one input: a positive integer t (1 <= t <= 10^4)
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: The value of `_` is `t-1`, `t` remains unchanged.

#Overall this is what the function does:Reads a positive integer from standard input and executes another function (`func_1`) that many times, leaving the input integer unchanged.

