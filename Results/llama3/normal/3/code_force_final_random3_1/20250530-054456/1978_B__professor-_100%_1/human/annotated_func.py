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
        
    #State: t is 0, stdin is empty.

#Overall this is what the function does:This function reads multiple lines of input from stdin, where the first line contains a single integer t, and each of the following t lines contains three integers n, a, and b. It then calculates and prints the sum of a sequence of numbers based on the values of n, a, and b, considering three different cases: when b is less than or equal to a, when b minus a is greater than or equal to n, and when b minus a is less than n. After processing all input lines, the function leaves stdin empty and t as 0.

