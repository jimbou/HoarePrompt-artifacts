#State of the program right berfore the function call: stdin contains a number of test cases t, each test case contains two integers n and q, a list of n integers a_1,\dots,a_n, and q queries, each query containing two integers l and r.
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
        
    #State: idx is n+2*q+n+2*q+...+n+2*q+t times, q is 0, results is a list containing 'YES' if x is 0, otherwise results is a list containing 'YES' and either 'YES' or 'NO' for each iteration of the loop and an empty string and either 'YES' or 'NO' and either 'YES' or 'NO' and ... and either 'YES' or 'NO' and an empty string, _ is q.
    print('\n'.join(results))
    #This is printed: A series of lines, each containing either 'YES' or 'NO', separated by empty lines, with the initial line containing 'YES' if x is 0, and the subsequent lines following the pattern of either 'YES' or 'NO' and an empty line, repeated for t iterations

#Overall this is what the function does:This function reads input from standard input, processes it according to a specific format, and prints the results. It expects the input to contain a number of test cases, each consisting of two integers (n and q), a list of n integers, and q queries, each containing two integers (l and r). The function then performs a series of operations on the input data, including XOR operations, prefix sum calculations, and binary searches. Based on the results of these operations, it appends either 'YES' or 'NO' to a list of results, which is then printed to standard output, separated by empty lines. The function effectively determines whether a given query can be satisfied based on the input data and prints the corresponding result.

