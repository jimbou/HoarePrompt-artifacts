#State of the program right berfore the function call: stdin contains a series of inputs: the first line contains an integer t (1 <= t <= 10^4), then for each test case, the first line contains two integers n and q (1 <= n, q <= 3 * 10^5), the second line contains n integers c_1, c_2, ..., c_n (1 <= c_i <= 10^9), and then q lines each containing two integers l_i and r_i (1 <= l_i <= r_i <= n).
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
        
    #State: The output state after the loop executes all the iterations is a series of 'YES' or 'NO' for each test case, indicating whether the condition s - (b - a + 1) >= i is met for the given range [a, b]. The number of 'YES' or 'NO' outputs is equal to the number of test cases (t) multiplied by the number of queries (m) for each test case. The state of the other variables in the precondition remains unchanged.

#Overall this is what the function does:This function processes a series of test cases from standard input, where each test case consists of an array of integers and a set of queries. For each query, it checks if a certain condition is met within a specified range of the array and outputs 'YES' if the condition is satisfied, 'NO' otherwise. The function iterates through all test cases and queries, producing a series of 'YES' or 'NO' outputs indicating the result of each query.

