#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^4). Each of the following t lines contains three integers n, a, and b (1 <= n, a, b <= 10^9).
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
        
    #State: The output will be t lines, each containing a single integer which is the maximum sum of n integers that can be obtained by selecting either a or b, where the sum is calculated as the sum of the first k integers from b to b-k+1 (where k is the minimum of b-a+1 and n) plus the sum of the remaining n-k integers as a.

#Overall this is what the function does:Calculates and prints the maximum sum of n integers that can be obtained by selecting either a or b for each of t test cases, where the sum is calculated as the sum of the first k integers from b to b-k+1 (where k is the minimum of b-a+1 and n) plus the sum of the remaining n-k integers as a, or simply n times a if a is greater than or equal to b.

