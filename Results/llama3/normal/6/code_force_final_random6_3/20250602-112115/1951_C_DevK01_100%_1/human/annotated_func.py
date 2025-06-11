#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines of inputs. The first line contains three integers n, m, and k (1 ≤ n ≤ 3*10^5, 1 ≤ m ≤ 10^9, 1 ≤ k ≤ min(nm, 10^9)). The second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9).
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
        
    #State: The loop has finished executing, t is 0, stdin is empty, and the program has printed the cost for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines of input. The first line contains three integers: n, m, and k. The second line contains n integers. The function calculates the minimum cost for each test case based on the given integers and prints the cost for each test case. The function continues this process until all test cases have been processed, at which point the program has printed the cost for each test case and standard input is empty.

