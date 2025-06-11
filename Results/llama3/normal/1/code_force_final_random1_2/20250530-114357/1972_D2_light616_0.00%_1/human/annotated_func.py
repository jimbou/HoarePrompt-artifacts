#State of the program right berfore the function call: stdin contains two inputs: first an integer and then two space-separated positive integers n and m such that 1 <= n, m <= 2 * 10^6.
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
        
    #State: x is less than or equal to the square root of n, cnt is greater than or equal to the sum of min(n / ((x + y) * x), m // ((x + y) * y)) for all x and y such that x * x <= n and (x + y) * x <= n and (x + y) * y <= m and math.gcd(x, y) == 1, n is greater than or equal to 1, m is greater than or equal to 1, y is greater than or equal to 1, stdin contains 1 input: an integer.
    print(cnt)
    #This is printed: cnt (where cnt is the count of the sum of min(n / ((x + y) * x), m // ((x + y) * y)) for all x and y such that x * x <= n and (x + y) * x <= n and (x + y) * y <= m and math.gcd(x, y) == 1)

#Overall this is what the function does:Calculates and prints the count of pairs of coprime numbers (x, y) such that (x + y) * x <= n and (x + y) * y <= m, where n and m are input integers, and returns the total count.

#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 10^4) followed by t lines, each containing two positive integers n and m (1 ≤ n, m ≤ 2 * 10^6).
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` is an integer between 1 and 10^4, stdin contains t lines, each containing two positive integers n and m (1 ≤ n, m ≤ 2 * 10^6), _ is t-1, and the function `func_1()` has been executed.

#Overall this is what the function does:Reads an integer t from standard input, then reads t lines from standard input, each containing two positive integers n and m, and executes the function func_1() t times.

