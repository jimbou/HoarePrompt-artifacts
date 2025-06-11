#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains three integers n, m, and k (1 <= n <= 3 * 10^5, 1 <= m <= 10^9, 1 <= k <= min(n*m, 10^9)). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
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
        
    #State: The loop has finished executing, and the program has continued to the next line of code. The value of t is 0, and the values of the other variables are unchanged. The loop has processed all the test cases, and the costs have been printed for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains three integers n, m, and k, and the second line contains n integers. The function calculates the cost for each test case based on the given integers and prints the cost. The cost calculation involves sorting the integers, selecting a subset of them, and performing arithmetic operations. The function processes all test cases and prints the corresponding costs.

