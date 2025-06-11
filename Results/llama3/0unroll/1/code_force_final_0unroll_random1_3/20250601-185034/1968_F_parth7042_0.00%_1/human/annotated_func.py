#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer t, then two integers n and q, and then a list of n integers. The last input is q pairs of integers.
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
        
    #State: idx is updated to the end of the data, results contains the answers to all the test cases, and the rest of the variables remain unchanged.
    print('\n'.join(results))
    #This is printed: the answers to all the test cases, each on a separate line

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer t, two integers n and q, a list of n integers, and q pairs of integers. It then processes each test case by calculating the prefix XOR of the list of integers and storing the indices of each XOR value in a dictionary. For each query pair (l, r), it checks if there exists an index i such that l <= i <= r and the XOR of the prefix up to i is equal to the XOR of the prefix up to r. If such an index exists, it appends 'YES' to the results list; otherwise, it appends 'NO'. Finally, it prints the results for all test cases, with each result on a separate line.

