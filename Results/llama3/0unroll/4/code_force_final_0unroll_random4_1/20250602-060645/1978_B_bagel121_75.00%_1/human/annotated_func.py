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
        
    #State: The output will be `t` lines, each containing a single integer, which is the maximum sum of `n` numbers that can be obtained by choosing `a` and `b` as the first two numbers, and then choosing the remaining numbers from the range `[a, b]` in a way that maximizes the sum.

#Overall this is what the function does:The function reads input from stdin, expecting multiple lines of input. It first reads an integer t, representing the number of test cases. For each test case, it reads three integers n, a, and b, and calculates the maximum sum of n numbers that can be obtained by choosing a and b as the first two numbers and then selecting the remaining numbers from the range [a, b] to maximize the sum. The function prints the maximum sum for each test case, resulting in t lines of output, each containing a single integer.

