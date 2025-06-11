#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^4). Each of the following t lines contains three integers n, a, and b (1 <= n, a, b <= 10^9).
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        
        if b <= a:
            print(n * a)
        elif b - a >= n:
            print(int((2 * b - n + 1) * n // 2))
        else:
            print(int((b - a) * (b - a + 1) // 2 + a * n))
        
    #State: The output state will contain `t` lines, each containing a single integer, which is the maximum sum of `n` numbers in an arithmetic progression with first term `a` and common difference `b`.

#Overall this is what the function does:This function reads multiple lines of input from stdin, where the first line contains an integer t, representing the number of test cases. For each test case, it reads three integers n, a, and b, and calculates the maximum sum of n numbers in an arithmetic progression with first term a and common difference b. It then prints the result for each test case. The function handles three cases: when b is less than or equal to a, when b minus a is greater than or equal to n, and when b minus a is less than n. The output will contain t lines, each with a single integer representing the maximum sum for each test case.

