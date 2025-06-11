#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines of input. The first line contains three integers n, m, and k (1 <= n <= 3*10^5, 1 <= m <= 10^9, 1 <= k <= min(n*m, 10^9)). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
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
        
    #State: t is 0, _ is t, stdin is empty, n is q if n * m equals k, otherwise n is the length of N, m is the minimum of the original m and k, k is the same as the original k, L is a list of three integers n, m, and k, M is a sorted list of n integers a_1, a_2, ..., a_n, N is a list of the q smallest integers from M if n * m equals k, otherwise N is a list of the q-1 smallest integers from M, q is the ceiling of k/m, w is the largest integer from N if n * m does not equal k, mu is k - (n - 1) * m if n * m does not equal k, and cost is m * sum(N) + m * m * ((n - 1) * n // 2) if n * m equals k, otherwise cost is mu * w + m * sum(N) + m * m * ((n - 1) * (n - 2) // 2) + n * m * mu.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines of input. The first line contains three integers n, m, and k, and the second line contains n integers a_1, a_2, ..., a_n. The function calculates the minimum cost based on the given integers and prints the result for each test case. The cost is calculated by sorting the integers, selecting the smallest q integers, and applying a formula that depends on whether n * m equals k or not. The function processes all test cases and empties the standard input.

