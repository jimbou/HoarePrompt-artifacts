#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of three inputs: first an integer t, then two integers n and q, and then a list of n integers. The list of integers is followed by q queries, each query consisting of two integers l and r. All integers are non-negative and 1 <= l <= r <= n.
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
        
    #State: The loop has executed for all the test cases in the input, and the program has printed 'YES' or 'NO' for each query in each test case based on the conditions. The input has been fully consumed, and the variables n, m, l, p, c, i, j, x, a, b, and s have been reset for each test case.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of an integer list and queries on that list. For each query, it determines whether a certain condition is met based on the sum of elements and the count of ones in the specified range, and prints 'YES' or 'NO' accordingly. The function consumes all input and resets variables for each test case, ultimately printing a 'YES' or 'NO' response for each query in every test case.

