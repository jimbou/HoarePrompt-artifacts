#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers n, a, and b (1 <= n, a, b <= 10^9).
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
        
    #State: t is an integer (0 <= t <= 10^9), n is an integer (1 <= n <= 10^9), a is an integer (1 <= a <= 10^9), b is an integer (1 <= b <= 10^9), stdin contains no test cases. If a >= b, the product of n and a is printed. Otherwise, k is the minimum of b - a + 1 and n, ans is the sum of the arithmetic series from b - k + 1 to b, p2 is the product of n - k and a, and ans + p2 is printed.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of three integers n, a, and b. For each test case, it calculates and prints the maximum sum that can be obtained by selecting k numbers from the range [a, b] and the remaining n-k numbers from a. If a is greater than or equal to b, it simply prints the product of n and a. Otherwise, it calculates the sum of the arithmetic series from b-k+1 to b and adds the product of n-k and a, then prints the result.

