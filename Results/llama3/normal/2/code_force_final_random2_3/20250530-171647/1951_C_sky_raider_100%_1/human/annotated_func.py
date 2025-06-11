#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines of input. The first line contains three integers n, m, and k (1 <= n <= 3 * 10^5, 1 <= m <= 10^9, 1 <= k <= min(n*m, 10^9)). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
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
        
    #State: n is 0, m is an integer, k is an integer minus the sum of s for all iterations, l is a sorted list of integers, t is the sum of s for all iterations, s is the minimum of m and k, c is the sum of s times the sum of the i-th element of l and the original value of t for all iterations, i is -1, and the integer value of c is being printed

#Overall this is what the function does:This function reads multiple test cases from standard input, each consisting of two lines. The first line contains three integers n, m, and k, and the second line contains n integers. It sorts the integers, then iterates through them, calculating a sum c by multiplying the minimum of m and k by the sum of the current integer and a running total t, and adding this product to c. The function prints the integer value of c for each test case.

