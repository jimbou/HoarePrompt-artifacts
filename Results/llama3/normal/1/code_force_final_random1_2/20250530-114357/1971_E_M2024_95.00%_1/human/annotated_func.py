#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four lines. The first line contains three integers n, k, and q, where k <= n <= 10^9 and 1 <= k, q <= 10^5. The second line contains k integers a_i, where 1 <= a_i <= n and a_i < a_{i+1} for every 1 <= i <= k-1 and a_k = n. The third line contains k integers b_i, where 1 <= b_i <= 10^9 and b_i < b_{i+1} for every 1 <= i <= k-1. Each of the following q lines contains a single integer d, where 0 <= d <= n.
    t = int(input())
    for _ in range(t):
        n, k, q = map(int, input().split())
        
        a = [0] + list(map(int, input().split()))
        
        b = [0] + list(map(int, input().split()))
        
        ad = [0]
        
        bd = [0]
        
        for i in range(1, len(a)):
            ad.append(a[i] - a[i - 1])
        
        for i in range(1, len(b)):
            bd.append(b[i] - b[i - 1])
        
        v = [0]
        
        for i in range(1, len(a)):
            v.append(ad[i] / bd[i])
        
        for l in range(q):
            m = 0
            i = 1
            ql = int(input())
            s = bisect_left(a, ql)
            if a[s] == ql:
                print(b[s], end=' ')
                continue
            ql -= a[s - 1]
            m += b[s - 1]
            m += bd[s] * ql / ad[s]
            print(int(m), end=' ')
        
        print()
        
    #State: t is an integer greater than or equal to 0, _ is t, n is an integer, k is an integer, q is 0, a is a list of n+1 integers, b is a list of n+1 integers, ad is a list containing n+1 integers 0 and the differences between consecutive elements of a, bd is a list containing n+1 integers 0 and the differences between consecutive elements of b, v is a list containing n+1 elements: 0 and the ratios of the differences between consecutive elements of a and b, i is 1, stdin contains 0 test cases, l is 0, and nothing is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains four lines of input. It processes each test case by calculating the differences between consecutive elements in two lists, computing the ratios of these differences, and then using these ratios to estimate the value of a function at a given point. The function prints the estimated values for each test case. After processing all test cases, the function leaves the input stream empty and does not return any value.

