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
        
    #State: Output State: The output state after the loop executes all the iterations is the same as the initial state, with the only difference being that the variable `t` has been decremented by the number of iterations of the loop. The value of `t` is now equal to the number of test cases minus the number of iterations of the loop. The values of the other variables in the precondition remain unchanged.

#Overall this is what the function does:This function reads multiple test cases from standard input, each containing three integers (n, m, k) and a list of n integers. It calculates the minimum cost for each test case based on the given integers and list, and prints the result. The function iterates through all test cases, and after execution, the output state remains the same as the initial state, with the only difference being the consumption of input test cases.

