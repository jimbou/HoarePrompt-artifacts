#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains three integers n, m, and k (1 <= n <= 3*10^5, 1 <= m <= 10^9, 1 <= k <= min(n*m, 10^9)). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
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
        
    #State: n is 0, i is n, m is an integer, k is an integer minus n times min(m, k), l is a sorted list of integers, t is n times min(m, k), s is min(m, k), c is the sum of n times s * (l[i] + (n-1) times min(m, k)), and the integer value of c which is the sum of n times s * (l[i] + (n-1) times min(m, k)) is being printed

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains three integers: n, m, and k. The second line contains n integers. The function sorts these n integers, then calculates a sum c by iterating over the sorted list, adding the product of the current integer and the minimum of m and k, and updating the value of k. Finally, the function prints the calculated sum c for each test case.

