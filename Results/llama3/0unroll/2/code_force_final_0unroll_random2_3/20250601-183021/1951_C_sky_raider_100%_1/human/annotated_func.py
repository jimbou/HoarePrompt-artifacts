#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains three space-separated integers: n, m, and k, where n is the number of sale days, m is the maximum amount of ticket purchasable each day, and k is the number of tickets to be bought at the end. The second line contains n space-separated integers: a_1, a_2, ..., a_n, representing the price per ticket for each of the upcoming n days.
    for i in range(int(input())):
        n, m, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        l.sort()
        
        t = 0
        
        s = 0
        
        c = 0
        
        for i in range(n):
            s = min(m, k)
            c += s * (l[i] + t)
            t += s
            k -= s
        
        print(int(c))
        
    #State: The total cost of buying k tickets over n days, with a maximum of m tickets purchasable each day, considering the prices per ticket for each day in ascending order.

#Overall this is what the function does:Calculates the total cost of buying a specified number of tickets over a given number of days, with a daily limit on ticket purchases, considering the prices per ticket for each day in ascending order.

