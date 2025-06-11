#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines of input. The first line contains three integers n, m, and k, where n is the number of sale days, m is the maximum amount of ticket purchasable each day, and k is the number of tickets to be bought at the end. The second line contains n integers a_1, a_2, ..., a_n, where a_i is the price per ticket for each of the upcoming n days.
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
        
    #State: The output state is the total cost of buying k tickets over n days, considering the maximum purchase limit m and the prices per ticket for each day. The cost is calculated by summing up the prices of the cheapest q days, where q is the minimum of m and k, and then adding the cost of buying the remaining tickets at the highest price. The output is the total cost for each test case.

#Overall this is what the function does:Calculates the total cost of buying k tickets over n days, considering the maximum purchase limit m and the prices per ticket for each day, and prints the total cost for each test case.

