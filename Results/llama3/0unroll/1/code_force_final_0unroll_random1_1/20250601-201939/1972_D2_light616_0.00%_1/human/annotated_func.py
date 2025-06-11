#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two positive integers n and m separated by a space, where 1 <= n, m <= 2 * 10^6.
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
        
    #State: cnt is the number of pairs (a, b) such that 1 <= a <= n, 1 <= b <= m, and gcd(a, b) = 1.
    print(cnt)
    #This is printed: cnt (where cnt is the number of pairs (a, b) such that 1 <= a <= n, 1 <= b <= m, and gcd(a, b) = 1)

#Overall this is what the function does:This function reads two positive integers n and m from standard input, calculates the number of pairs (a, b) such that 1 <= a <= n, 1 <= b <= m, and gcd(a, b) = 1, and prints the result.

#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing two positive integers n and m (1 <= n, m <= 2 * 10^6).
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: t is 0, stdin contains t lines, each containing two positive integers n and m (1 <= n, m <= 2 * 10^6).

#Overall this is what the function does:Reads an integer t from standard input, then reads t lines, each containing two positive integers n and m, and performs some unknown action for each line (as the implementation of func_1 is not provided).

