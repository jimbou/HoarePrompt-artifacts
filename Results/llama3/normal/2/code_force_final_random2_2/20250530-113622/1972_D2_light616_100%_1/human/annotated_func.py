#State of the program right berfore the function call: stdin contains multiple lines of input: the first line contains a positive integer t, and each of the following lines contains two positive integers n and m.
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
        
    #State: x is the square root of n rounded up, y is n + 1, cnt is the sum of the minimum of n // ((i + j) * i) and m // ((i + j) * j) for all i from 1 to the square root of n rounded up inclusive and all j from 1 to n inclusive where the greatest common divisor of i and j is 1.
    print(cnt)
    #This is printed: cnt (where cnt is the sum of the minimum of n // ((i + j) * i) and m // ((i + j) * j) for all i from 1 to the square root of n rounded up inclusive and all j from 1 to n inclusive where the greatest common divisor of i and j is 1)

#Overall this is what the function does:This function reads two positive integers n and m from the standard input, calculates the sum of the minimum of n // ((i + j) * i) and m // ((i + j) * j) for all i from 1 to the square root of n rounded up inclusive and all j from 1 to n inclusive where the greatest common divisor of i and j is 1, and prints the result.

#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 10^4) followed by t lines, each containing two positive integers n and m (1 ≤ n, m ≤ 2 * 10^6).
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `_` is `t-1`, `t` is an integer between 1 and 10^4, stdin contains `t - t` lines, each containing two positive integers `n` and `m` (1 ≤ n, m ≤ 2 * 10^6), and the function `func_1()` has been executed.

#Overall this is what the function does:Reads an integer t from standard input, then reads t lines of input, each containing two positive integers n and m, and executes the function func_1() for each line, without returning any value or modifying the input variables.

