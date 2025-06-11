#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains three space-separated integers: n, m, and k, where n is the number of sale days, m is the maximum amount of ticket purchasable each day, and k is the number of tickets to be bought at the end. The second line contains n space-separated integers: a_1, a_2, ..., a_n, where a_i is the price per ticket for each of the upcoming n days.
    for i in range(int(input())):
        n, m, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        l.sort()
        
        s = 0
        
        c = k * k / 2
        
        for i in range(n):
            s = min(m, k)
            k -= s
            c += l[i] * s - s * s / 2
        
        print(int(c))
        
    #State: The output state is the total cost of buying k tickets over n days, considering the price per ticket for each day and the maximum amount of tickets that can be bought each day. The total cost is calculated by summing up the cost of buying the minimum of m or k tickets each day, where the cost is the price per ticket multiplied by the number of tickets bought, minus the sum of the first s natural numbers (s*(s-1)/2), where s is the number of tickets bought. The output is the total cost after all iterations of the loop.

#Overall this is what the function does:This function calculates the total cost of buying a specified number of tickets over a series of days, considering daily ticket price limits and a maximum daily purchase limit. It takes no arguments and returns the total cost as output, processing multiple test cases from standard input.

