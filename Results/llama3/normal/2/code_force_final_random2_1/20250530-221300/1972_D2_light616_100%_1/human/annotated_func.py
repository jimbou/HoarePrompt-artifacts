#State of the program right berfore the function call: n and m are positive integers less than or equal to 2 * 10^6.
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
        
    #State: x is the smallest integer greater than or equal to the square root of n, y is the smallest integer greater than or equal to the square root of m, cnt is the sum of min(n // ((x + y) * x), m // ((x + y) * y)) for all x from 1 to the value of x in the output state and for all y from 2 to the value of y in the output state, such that math.gcd(x, y) == 1.
    print(cnt)
    #This is printed: cnt (where cnt is the sum of min(n // ((x + y) * x), m // ((x + y) * y)) for all x from 1 to the smallest integer greater than or equal to the square root of n, and for all y from 2 to the smallest integer greater than or equal to the square root of m, such that math.gcd(x, y) == 1)

#Overall this is what the function does:Calculates and prints the sum of minimum values obtained by dividing two input numbers (n and m) by the product of two coprime numbers (x and y), where x ranges from 1 to the square root of n and y ranges from 2 to the square root of m.

#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a positive integer t. Each of the following lines contains two positive integers n and m, separated by a space, such that 1 <= n, m <= 2 * 10^6.
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` is 0, stdin contains multiple lines of input. The first line contains two positive integers n and m, separated by a space, such that 1 <= n, m <= 2 * 10^6, and the function `func_1()` has been executed and returned None.

#Overall this is what the function does:Reads a positive integer t from standard input, then reads t pairs of positive integers n and m from standard input, and executes a function func_1() for each pair, without returning any value.

