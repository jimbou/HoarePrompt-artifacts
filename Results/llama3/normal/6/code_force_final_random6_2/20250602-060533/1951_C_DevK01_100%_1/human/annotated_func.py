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
            cost += m * sum(N) + m * m * ((n - 1) * n // 2) + n * m * mu
        
        print(cost)
        
        continue
        
    #State: t is 0, _ is t, stdin is empty, n is q, m is the minimum of the original m and k, M is sorted, N is the first q elements of the sorted M, q is the ceiling of k divided by m. If the product of the current value of n and the current value of m equals k, then cost is m * sum(N) + m * m * ((n - 1) * n // 2). Otherwise, n is the length of N, m is the minimum of the original m and k, M is sorted, N is the first q-1 elements of the sorted M, q is the ceiling of k divided by m, and n * m is not equal to k, w is the last element of the original N, mu is k - (q - 1) * m, cost is mu * w + m * sum(N) + m * m * ((q - 2) * (q - 1) // 2) + (q - 1) * m * mu, and cost is printed, and we skip the rest of the current iteration of the loop.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains three integers n, m, and k, and the second line contains n integers a_1, a_2, ..., a_n. For each test case, it calculates a cost based on the given integers and prints the result. The cost is calculated by first sorting the integers a_1, a_2, ..., a_n and then selecting a subset of the sorted integers. If the product of the number of selected integers and m equals k, the cost is calculated as m times the sum of the selected integers plus m squared times the sum of the first n-1 positive integers. Otherwise, the cost is calculated as the product of the last selected integer and the difference between k and the product of the number of selected integers minus one and m, plus m times the sum of the selected integers minus the last one, plus m squared times the sum of the first n-2 positive integers, plus the product of the number of selected integers minus one, m, and the difference between k and the product of the number of selected integers minus one and m.

