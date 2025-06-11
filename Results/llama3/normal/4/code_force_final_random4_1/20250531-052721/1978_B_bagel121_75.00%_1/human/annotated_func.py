#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 10^4). Each of the following t lines contains three integers n, a, and b (1 <= n, a, b <= 10^9).
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        
        if a >= b:
            print(n * a)
        else:
            k = min(b - a + 1, n)
            ans = int((b + (b - k + 1)) / 2 * k)
            p2 = (n - k) * a
            print(ans + p2)
        
    #State: t is an integer between 1 and 10^4, _ is equal to t, t must be greater than or equal to 0, n is an integer between 1 and 10^9, a is an integer between 1 and 10^9, b is an integer between 1 and 10^9, stdin is empty. If a is greater than or equal to b, the product of n and a is printed. Otherwise, the sum of ans and p2 is printed.

#Overall this is what the function does:This function reads a series of input lines from stdin, where the first line contains an integer t, representing the number of test cases. For each test case, it reads three integers n, a, and b, and calculates the sum of the products of n and a, or the sum of the arithmetic series from b to b-k+1 and the product of (n-k) and a, depending on whether a is greater than or equal to b. It then prints the calculated sum for each test case, until all t test cases have been processed, leaving stdin empty.

