#State of the program right berfore the function call: stdin contains a number of test cases t, each test case contains an integer n, an array a of n integers, an integer q, and q queries, each query contains two integers l and r. 1 <= t <= 10^4, 2 <= n <= 2 * 10^5, 1 <= a_i <= 10^6, 1 <= q <= 2 * 10^5, 1 <= l < r <= n.
    R = lambda : map(int, input().split())
    t, = R()
    while t:
        t -= 1
        
        R()
        
        a = [0]
        
        p = i = j = 0
        
        for x in R():
            j = (j, i)[x != p]
            a += j,
            p = x
            i += 1
        
        q, = R()
        
        while q:
            q -= 1
            l, r = R()
            print(*((a[r], r), [-1] * 2)[a[r] < l])
        
    #State: t is 0, stdin contains 0 test cases, a is a list of length equal to the number of elements in the last R() plus 1, p is the last element in the last R(), i is equal to the number of elements in the last R(), j is either 0 or i depending on whether the last element in the last R() is equal to the second last element in the last R(), q is 0, l is the first element in the last R(), r is the second element in the last R(), and for each query in the original q queries, if the value of a at index r is less than l, then -1 is printed twice, otherwise the value of a at index r and r are printed

#Overall this is what the function does:This function reads a number of test cases from standard input, where each test case consists of an integer n, an array a of n integers, an integer q, and q queries, each containing two integers l and r. For each query, it prints the value of a at index r and r if a[r] is greater than or equal to l, otherwise it prints -1 twice. The function processes all test cases and queries, and upon completion, the standard input is exhausted, and all queries have been processed and printed accordingly.

