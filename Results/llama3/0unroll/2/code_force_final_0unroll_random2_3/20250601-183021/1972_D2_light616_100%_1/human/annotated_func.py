#State of the program right berfore the function call: stdin contains multiple test cases, each test case contains two positive integers n and m, separated by a space, where 1 <= n, m <= 2 * 10^6.
    x = 1
    cnt = 0
    n, m = map(int, input().split())
    while x * x <= n:
        y = 1
        
        while (x + y) * x <= n and (x + y) * y <= m:
            if math.gcd(x, y) == 1:
                cnt += min(n // ((x + y) * x), m // ((x + y) * y))
            y += 1
        
        x += 1
        
    #State: cnt is the number of coprime pairs (a, b) where 1 <= a <= n and 1 <= b <= m, x is the smallest integer greater than the square root of n, y is 1.
    print(cnt)
    #This is printed: cnt (where cnt is the number of coprime pairs (a, b) where 1 <= a <= n and 1 <= b <= m)

#Overall this is what the function does:Calculates and prints the number of coprime pairs (a, b) where 1 <= a <= n and 1 <= b <= m, given two positive integers n and m as input, and returns no value.

#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing two positive integers n and m (1 <= n, m <= 2 * 10^6).
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: The loop has executed `t` times, and the function `func_1()` has been called `t` times. The values of `n` and `m` have been read from stdin `t` times, but their values are not retained after each iteration. The state of other variables in the precondition remains unchanged.

#Overall this is what the function does:Reads an integer t from standard input, then reads t pairs of positive integers n and m, and calls the function func_1() t times, without retaining the values of n and m after each iteration.

