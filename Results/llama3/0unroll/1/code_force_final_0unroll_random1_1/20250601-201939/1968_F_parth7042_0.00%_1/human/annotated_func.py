#State of the program right berfore the function call: stdin contains a series of test cases. Each test case contains three lines of input: the first line contains two integers n and q, the second line contains n integers a_1, ..., a_n, and the next q lines each contain two integers l and r. The input values are non-negative integers, 1 <= n <= 2 * 10^5, 1 <= q <= 2 * 10^5, 0 <= a_i < 2^30, 1 <= l < r <= n.
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        
        q = int(data[idx + 1])
        
        idx += 2
        
        a = [0] * (n + 1)
        
        pf = [0] * (n + 1)
        
        mp = {(0): [0]}
        
        for i in range(1, n + 1):
            a[i] = int(data[idx])
            idx += 1
            pf[i] = pf[i - 1] ^ a[i]
            if pf[i] not in mp:
                mp[pf[i]] = []
            mp[pf[i]].append(i)
        
        for _ in range(q):
            l = int(data[idx])
            r = int(data[idx + 1])
            idx += 2
            x = pf[r] ^ pf[l - 1]
            if x == 0:
                results.append('YES')
                continue
            v1 = mp.get(pf[r], [])
            v2 = mp.get(pf[l - 1], [])
            it1 = bisect.bisect_left(v1, l)
            it2 = bisect.bisect_left(v2, r) - 1
            if it1 < len(v1) and it2 >= 0 and v1[it1] <= r and v2[it2] >= l:
                results.append('YES')
            else:
                results.append('NO')
        
        results.append('')
        
    #State: Output State: stdin is empty, t is 0, results is a list of strings containing 'YES' or 'NO' for each query, and idx is equal to the length of data plus 1.
    print('\n'.join(results))
    #This is printed: A string containing 'YES' or 'NO' for each query, separated by newline characters (where 'YES' or 'NO' are the results of the queries)

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case contains a list of integers and a set of queries. It processes each query by checking if there exists a subarray within the given range that has a XOR value equal to the XOR value of the entire range. If such a subarray exists, it outputs 'YES', otherwise 'NO'. The function outputs the results of all queries, separated by newline characters, and leaves the standard input empty.

