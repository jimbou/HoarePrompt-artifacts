#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains three integers n, m, and k (1 <= n <= 3*10^5, 1 <= m <= 10^9, 1 <= k <= min(n*m, 10^9)). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    t = int(input())
    for _ in range(t):
        L = list(map(int, input().split()))
        
        M = list(map(int, input().split()))
        
        n, m, k = L[0], L[1], L[2]
        
        m = min(m, k)
        
        M.sort()
        
        q = int(math.ceil(k / m))
        
        N = M[:q]
        
        n = len(N)
        
        if n * m == k:
            cost = m * sum(N) + m * m * ((n - 1) * n // 2)
        else:
            w = N.pop()
            mu = k - (n - 1) * m
            cost = mu * w
            n = len(N)
            cost += m * sum(N) + m * m * ((n - 1) * (n - 2) // 2) + n * m * mu
        
        print(cost)
        
        continue
        
    #State: The loop has executed t times, and for each execution, it has read two lines from the standard input, processed the input data, and printed the calculated cost to the standard output. The values of the variables t, n, m, k, L, M, q, N, w, mu, and cost have been updated accordingly after each iteration. The state of the other variables in the precondition that are not affected by the loop head and body remains unchanged.

#Overall this is what the function does:Calculates and prints the minimum cost for each test case, where the cost is determined by the sum of the products of the number of items and their respective costs, considering the constraints of the number of items, the maximum cost, and the number of test cases.

