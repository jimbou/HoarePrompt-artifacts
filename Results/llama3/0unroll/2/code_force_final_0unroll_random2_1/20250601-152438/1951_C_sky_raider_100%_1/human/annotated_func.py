#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains three integers n, m, and k (1 <= n <= 3 * 10^5, 1 <= m <= 10^9, 1 <= k <= min(nm, 10^9)). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
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
        
    #State: The output state after the loop executes all the iterations is the sum of the products of the minimum of m and k, and the sum of the current element in the list and the total sum so far, for each element in the sorted list. The total sum is updated by adding the product of the minimum of m and k, and the current element in the list, and the minimum of m and k is subtracted from k. The output is the integer value of the total sum.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains three integers n, m, and k, and the second line contains n integers. The function sorts the integers, then iterates through them, calculating a total sum by adding the product of the minimum of m and k, and the sum of the current integer and the total sum so far. The total sum is updated and the minimum of m and k is subtracted from k in each iteration. Finally, the function prints the integer value of the total sum for each test case.

