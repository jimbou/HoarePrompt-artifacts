#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines of input. The first line contains three integers n, m, and k. The second line contains n integers a_1, a_2, ..., a_n. 1 <= n <= 3 * 10^5, 1 <= m <= 10^9, 1 <= k <= min(nm, 10^9), and 1 <= a_i <= 10^9.
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
        
    #State: `t` is an integer representing the number of test cases that must be greater than or equal to 0, stdin is empty, `_` is `t`, `n`, `m`, `k`, `M`, `L`, `N`, `q`, `w`, `mu`, and `cost` are undefined.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines of input. The first line contains three integers n, m, and k, and the second line contains n integers a_1, a_2, ..., a_n. For each test case, it calculates the minimum cost by sorting the integers, selecting a subset of the sorted integers, and performing arithmetic operations on the selected integers. The function then prints the calculated cost for each test case. After processing all test cases, the function leaves the standard input empty and undefined variables n, m, k, M, L, N, q, w, mu, and cost.

