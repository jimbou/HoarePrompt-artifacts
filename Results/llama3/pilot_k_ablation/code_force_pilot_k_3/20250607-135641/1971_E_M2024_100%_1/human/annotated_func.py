#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four inputs: first three integers n, k, and q, and then k integers a_i, k integers b_i, and q integers d. n, k, and q are positive integers such that k <= n <= 10^9 and 1 <= k, q <= 10^5. a_i and b_i are strictly increasing sequences of positive integers such that 1 <= a_i <= n, 1 <= b_i <= 10^9, a_k = n. d is a positive integer such that 0 <= d <= n.
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
        
    #State: t is 0, n is an integer, k is an integer, q is an integer and must be greater than or equal to 0, a is a list of integers with length q+1, b is a list of integers with length q+1, ad is a list with q+1 elements where the first element is 0 and the rest of the elements are the differences between consecutive elements in a, bd is a list with q+1 elements where the first element is 0 and the rest of the elements are the differences between consecutive elements in b, stdin is empty, i is 0, v is a list with q+1 elements, 0 and the rest of the elements are the divisions of the corresponding elements in ad and bd, l is 0, ql is an integer equal to the input minus a[s - 1], m is an integer equal to the sum of b[s - 1] and the product of bd[s] and ql divided by ad[s], s is an integer equal to the insertion point of ql in a to maintain sorted order, and nothing is printed

#Overall this is what the function does:This function reads multiple test cases from standard input, each containing four inputs: three integers n, k, and q, and then k integers a_i, k integers b_i, and q integers d. It processes each test case by calculating the differences between consecutive elements in a and b, and then uses these differences to compute the value of b corresponding to a given query value d. The function prints the computed values for each query in each test case.

