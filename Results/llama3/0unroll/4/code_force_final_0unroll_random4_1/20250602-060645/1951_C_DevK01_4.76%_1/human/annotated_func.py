#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines of input. The first line contains three integers n, m, and k, where n is the number of sale days, m is the maximum amount of ticket purchasable each day, and k is the number of tickets to be bought at the end. The second line contains n integers a_1, a_2, ..., a_n, which are the price per ticket for each of the upcoming n days.
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
        
    #State: Output State: The loop has executed all iterations, and the output state is the final state of the variables after the last iteration. The variables t, L, M, n, m, k, q, N, and cost have been updated according to the loop body. The final values of these variables are:
    #
    #* t: 0 (since the loop has executed all iterations)
    #* L: The last list of integers read from stdin, containing three integers n, m, and k.
    #* M: The last list of integers read from stdin, containing n integers a_1, a_2, ..., a_n.
    #* n: The number of sale days in the last test case.
    #* m: The minimum of the maximum amount of ticket purchasable each day and the number of tickets to be bought at the end in the last test case.
    #* k: The number of tickets to be bought at the end in the last test case.
    #* q: The number of days needed to buy k tickets in the last test case.
    #* N: The sorted list of prices per ticket for the first q days in the last test case.
    #* cost: The total cost of buying k tickets in the last test case.
    #
    #The output state is the final state of these variables after the last iteration of the loop.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines of input. The first line contains three integers: the number of sale days, the maximum amount of tickets purchasable each day, and the number of tickets to be bought at the end. The second line contains the price per ticket for each of the upcoming sale days. The function calculates the total cost of buying the specified number of tickets, considering the minimum of the maximum amount of tickets purchasable each day and the number of tickets to be bought at the end. It sorts the prices per ticket for the first q days, where q is the number of days needed to buy the specified number of tickets, and calculates the total cost based on the sorted prices. The function prints the total cost for each test case.

