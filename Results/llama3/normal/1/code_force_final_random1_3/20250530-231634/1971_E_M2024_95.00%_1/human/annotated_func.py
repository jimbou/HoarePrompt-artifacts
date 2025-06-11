#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four inputs: first a line with three integers n, k, and q, then a line with k integers a_i, then a line with k integers b_i, and finally q lines each with a single integer d. n and k are non-negative integers, 1 <= k <= n <= 10^9, 1 <= q <= 10^5, 1 <= a_i <= n, a_i < a_{i+1} for every 1 <= i <= k-1, a_k = n, 1 <= b_i <= 10^9, b_i < b_{i+1} for every 1 <= i <= k-1, and 0 <= d <= n. The sum of k over all test cases doesn't exceed 10^5, and the sum of q over all test cases doesn't exceed 10^5.
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
        
    #State: t is 0, _ is t, n is an integer, k is an integer, q is greater than or equal to 0, a is a list of integers with a length of at least len(a), b is a list of integers with a length of at least len(b), ad is a list containing len(a) integers, the first integer is 0, and the last len(a) - 1 integers are a[i] - a[i - 1] for i in range(1, len(a)), bd is a list containing len(b) integers, the first integer is 0, and the last len(b) - 1 integers are b[i] - b[i - 1] for i in range(1, len(b)), stdin contains 0 inputs, v is a list containing len(a) integers where the first integer is 0 and the remaining integers are ad[i] / bd[i] for i in range(1, len(a)), l is q, ql is an integer equal to the input value minus a[s - 1], s is the insertion point for ql in a to maintain sorted order, i is 1, and m is b[s - 1] plus bd[s] times ql divided by ad[s], and nothing is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, each containing four inputs: three integers n, k, and q, followed by k integers a_i, k integers b_i, and q lines each with a single integer d. It then calculates the differences between consecutive elements in a_i and b_i, and uses these differences to compute the value of b_i corresponding to a given input d. The function prints the computed values for each test case, separated by spaces, and followed by a newline character.

