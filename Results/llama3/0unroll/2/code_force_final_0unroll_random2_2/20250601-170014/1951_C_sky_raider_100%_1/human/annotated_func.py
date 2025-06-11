#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines of input. The first line contains three integers n, m, and k (1 <= n <= 3 * 10^5, 1 <= m <= 10^9, 1 <= k <= min(nm, 10^9)). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
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
        
    #State: The output state after the loop executes all the iterations is the sum of the products of the minimum of m and k, the current element in the sorted list l, and the cumulative sum t, for each element in the list l. The output is printed for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines: the first line contains three integers n, m, and k, and the second line contains n integers. It sorts the integers in ascending order, then iterates through the sorted list, calculating a cumulative sum by multiplying the minimum of m and k with the current integer and the cumulative sum, and adding the result to the total sum. The function prints the total sum for each test case.

