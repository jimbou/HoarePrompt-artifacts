#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer t, then two integers n and q, and then a list of n integers. The list of integers is followed by q queries, each query consisting of two integers l and r. The integers t, n, and q are positive. The integers in the list are positive. The integers l and r are positive and l <= r <= n.
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        p = [0]
        
        c = [0]
        
        i, j = 0, 0
        
        for x in l:
            if x == 1:
                j += 1
            i += x
            p.append(i)
            c.append(j)
        
        for _ in range(m):
            a, b = map(int, input().split())
            i = c[b] - c[a - 1]
            s = p[b] - p[a - 1]
            if b - a + 1 > 1 and s - (b - a + 1) >= i:
                print('YES')
            else:
                print('NO')
        
    #State: The output state will contain the results of all the test cases. Each test case will have a series of 'YES' or 'NO' outputs, one for each query. The 'YES' or 'NO' output for each query will depend on whether the condition `s - (b - a + 1) >= i` is met or not. If the condition is met, the output will be 'YES', otherwise it will be 'NO'. The number of 'YES' or 'NO' outputs for each test case will be equal to the value of `m` for that test case.

#Overall this is what the function does:This function processes multiple test cases from standard input. Each test case consists of an integer n, an integer m, a list of n integers, and m queries. The function calculates the cumulative sum and count of 1's in the list, then for each query, it checks if the sum of the elements in the query range minus the range length is greater than or equal to the count of 1's in the range. If the condition is met, it prints 'YES', otherwise it prints 'NO'. The function repeats this process for all test cases and queries, producing a series of 'YES' or 'NO' outputs.

