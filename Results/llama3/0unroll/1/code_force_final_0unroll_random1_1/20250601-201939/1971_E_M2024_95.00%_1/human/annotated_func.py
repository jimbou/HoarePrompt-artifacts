#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four inputs: first three integers n, k, and q, and then k integers a_i, k integers b_i, and q integers d. n, k, and q are non-negative integers such that 1 <= k, q <= 10^5 and k <= n <= 10^9. a_i and b_i are strictly increasing sequences of non-negative integers such that 1 <= a_i <= n, 1 <= b_i <= 10^9, a_k = n, and a_i < a_{i+1} and b_i < b_{i+1} for every 1 <= i <= k-1. d is a non-negative integer such that 0 <= d <= n.
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
        
    #State: The output state after the loop executes all the iterations is that the program will have processed all the test cases and printed the results for each query in each test case. The values of the variables in the loop head and body will have been updated accordingly, but the state of the other variables in the precondition that are not affected by the loop head and body will remain unchanged. Specifically, the values of `t`, `n`, `k`, `q`, `a`, `b`, `ad`, `bd`, and `v` will have been updated for each test case, and the results for each query will have been printed. The final output state will be the last printed result for the last query in the last test case.

#Overall this is what the function does:This function processes multiple test cases from standard input, each containing four inputs: three integers (n, k, q) and three sequences of integers (a, b, d). It calculates the differences between consecutive elements in sequences a and b, and then uses these differences to compute a new sequence v. For each query in each test case, it performs a binary search on sequence a to find the appropriate index, and then uses the corresponding values from sequences b and v to calculate and print the result. The function continues this process until all test cases and queries have been processed, printing the results for each query in each test case.

