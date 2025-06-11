#State of the program right berfore the function call: stdin contains multiple test cases. The first line of stdin contains an integer t (1 <= t <= 10^4) — the number of test cases. Each test case contains two lines. The first line of each test case contains three integers n, m, and k (1 <= n <= 3 * 10^5, 1 <= m <= 10^9, 1 <= k <= min(nm, 10^9)) — the number of sale days, the maximum amount of ticket purchasable each day, and the number of tickets to be bought at the end. The second line of each test case contains n integers a_1, a_2, …, a_n (1 <= a_i <= 10^9) — the price per ticket for each of the upcoming n days.
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
        
    #State: The loop will execute 't' number of times, where 't' is an integer between 1 and 10^4. In each iteration, it will read two lines of input from stdin, process the input, and print the calculated cost. After all iterations, the loop will terminate, and the program will continue executing any remaining code. The state of variables outside the loop will remain unchanged.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains three integers: the number of sale days, the maximum amount of tickets purchasable each day, and the number of tickets to be bought. The second line contains the price per ticket for each of the upcoming days. For each test case, it calculates the minimum cost to buy the specified number of tickets, considering the maximum amount of tickets that can be bought each day, and prints the calculated cost. The function repeats this process for the specified number of test cases.

