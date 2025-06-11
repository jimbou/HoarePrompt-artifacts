#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains three integers n, m, and k, where n is the number of sale days, m is the maximum amount of ticket purchasable each day, and k is the number of tickets to be bought at the end. The second line contains n integers a_1, a_2, ..., a_n, which are the price per ticket for each of the upcoming n days.
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
        
    #State: The loop will execute t times, and for each execution, it will read two lines of input from stdin. The first line will contain three integers n, m, and k, and the second line will contain n integers a_1, a_2, ..., a_n. The loop will calculate the minimum cost to buy k tickets over n days, considering the maximum number of tickets that can be bought each day (m) and the price per ticket for each day (a_1, a_2, ..., a_n). The calculated cost will be printed to the console. After all iterations, the loop will terminate, and the program will exit.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains three integers: the number of sale days, the maximum number of tickets that can be bought per day, and the total number of tickets to be bought. The second line contains the prices per ticket for each day. The function calculates the minimum cost to buy the specified number of tickets over the given days, considering the daily ticket limit, and prints the calculated cost to the console. The function repeats this process for each test case and then terminates.

