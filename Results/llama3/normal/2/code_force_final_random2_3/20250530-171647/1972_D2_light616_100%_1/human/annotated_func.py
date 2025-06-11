#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a positive integer t. Each subsequent line contains two positive integers n and m.
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
        
    #State: x is the smallest integer greater than the square root of n, y is m + 1, cnt is the sum of the minimum of n // ((x + y) * x) and m // ((x + y) * y) for all x and y such that x * x <= n and (x + y) * x <= n and (x + y) * y <= m and math.gcd(x, y) == 1.
    print(cnt)
    #This is printed: cnt (where cnt is the sum of the minimum of n // ((x + y) * x) and m // ((x + y) * y) for all x and y such that x * x <= n and (x + y) * x <= n and (x + y) * y <= m and math.gcd(x, y) == 1)

#Overall this is what the function does:This function reads two positive integers n and m from the standard input, calculates the sum of the minimum of n // ((x + y) * x) and m // ((x + y) * y) for all x and y such that x * x <= n and (x + y) * x <= n and (x + y) * y <= m and math.gcd(x, y) == 1, and prints the result.

#State of the program right berfore the function call: stdin contains one input: a positive integer t, representing the number of test cases.
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` is a positive integer greater than or equal to 0, stdin contains no input, and the function `func_1()` has been executed `t` times.

#Overall this is what the function does:Reads a positive integer t from standard input, executes the function func_1() t times, and leaves the standard input empty.

