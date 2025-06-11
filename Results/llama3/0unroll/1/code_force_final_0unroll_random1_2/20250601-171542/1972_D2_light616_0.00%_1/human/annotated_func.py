#State of the program right berfore the function call: stdin contains multiple lines of input: the first line contains a positive integer t (1 <= t <= 10^4), and each of the following t lines contains two positive integers n and m (1 <= n, m <= 2 * 10^6).
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
        
    #State: cnt is the number of coprime pairs (a, b) such that 1 <= a <= n and 1 <= b <= m, and x is the smallest integer such that x * x > n.
    print(cnt)
    #This is printed: cnt (the number of coprime pairs (a, b) such that 1 <= a <= n and 1 <= b <= m)

#Overall this is what the function does:This function reads two positive integers n and m from standard input, calculates the number of coprime pairs (a, b) such that 1 <= a <= n and 1 <= b <= m, and prints the result.

#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 10^4) followed by t lines, each containing two positive integers n and m (1 ≤ n, m ≤ 2 * 10^6).
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` is an integer between 0 and 10^4, stdin contains t lines, each containing two positive integers n and m (1 ≤ n, m ≤ 2 * 10^6)

#Overall this is what the function does:Reads an integer t from standard input, then reads t lines of input, each containing two positive integers n and m, and performs some unspecified action for each line of input.

