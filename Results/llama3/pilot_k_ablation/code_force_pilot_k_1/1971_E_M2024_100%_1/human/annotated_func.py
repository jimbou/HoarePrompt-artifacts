#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four inputs: first a line with three integers n, k, and q, then a line with k integers a_i, then a line with k integers b_i, and finally q lines with a single integer d. n, k, and q are non-negative integers such that 1 <= t <= 10^4, k <= n <= 10^9, and 1 <= k, q <= 10^5. a_i and b_i are strictly increasing sequences of non-negative integers such that 1 <= a_i <= n, 1 <= b_i <= 10^9, a_k = n, and the sum of k over all test cases doesn't exceed 10^5. The sum of q over all test cases doesn't exceed 10^5.
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
            m += bd[s] * ql // ad[s]
            print(m, end=' ')
        
        print()
        
    #State: t is 0, n, k, and q are non-negative integers such that k <= n <= 10^9, and 1 <= k, q <= 10^5. a is a strictly increasing sequence of non-negative integers such that 1 <= a_i <= n and a has at least 1 element, b is a strictly increasing sequence of non-negative integers such that 1 <= b_i <= 10^9, a_k = n, ad is a list with k elements: the first element is 0 and the rest of the elements are the differences between consecutive elements in a, bd is a list with k elements: the first element is 0 and the rest of the elements are the differences between consecutive elements in b, v is a list with k elements: the first element is 0 and the rest of the elements are the ratios of the differences between consecutive elements in a and b, and nothing is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, each containing four inputs: three integers n, k, and q, followed by two sequences of k integers a_i and b_i, and finally q single integers d. It then calculates the differences between consecutive elements in a and b, and the ratios of these differences. For each query integer d, it finds the corresponding value in the sequence b using binary search and prints the result. If d is equal to an element in a, it prints the corresponding element in b; otherwise, it calculates the result using the differences and ratios. The function processes all test cases and prints the results for each query.

