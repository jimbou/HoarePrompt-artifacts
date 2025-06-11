#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a positive integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each of the following lines contains two positive integers n and m (1 ≤ n, m ≤ 2 * 10^6) separated by a space.
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
        
    #State: x is the smallest integer greater than the square root of n, cnt is the total count of pairs (x, y) that satisfy the conditions (x + y) * x <= n, (x + y) * y <= m, and math.gcd(x, y) == 1, n is unchanged, m is unchanged, stdin contains no lines of input.
    print(cnt)
    #This is printed: cnt (where cnt is the total count of pairs (x, y) that satisfy the given conditions)

#Overall this is what the function does:This function reads two positive integers n and m from standard input, counts the number of pairs (x, y) that satisfy the conditions (x + y) * x <= n, (x + y) * y <= m, and math.gcd(x, y) == 1, and prints the total count.

#State of the program right berfore the function call: stdin contains one input: a positive integer (t) representing the number of test cases.
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: Output State: `t` is 0, stdin contains no input.

#Overall this is what the function does:Reads a positive integer from standard input, representing the number of test cases, and executes a function (func_1) for each test case, leaving the input stream empty and the test case counter at 0.

