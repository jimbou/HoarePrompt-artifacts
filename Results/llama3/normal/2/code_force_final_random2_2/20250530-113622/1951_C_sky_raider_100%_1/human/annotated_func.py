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
        
    #State: n is 0, m is an integer, l is a sorted list of integers, i is n, s is the minimum of m and k, t is the sum of the minimum of m and k for n iterations, c is the sum of the minimum of m and k times the sum of the elements of l and the minimum of m and k for n iterations, k is the difference of k and the sum of the minimum of m and k for n iterations, and the integer value of c is being printed

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines of input. The first line contains three integers n, m, and k, and the second line contains n integers. The function sorts the list of integers, then iterates over the sorted list, calculating a cumulative sum c by multiplying the minimum of m and k by the sum of the current integer and the cumulative sum of the minimum of m and k. The function prints the integer value of c for each test case.

