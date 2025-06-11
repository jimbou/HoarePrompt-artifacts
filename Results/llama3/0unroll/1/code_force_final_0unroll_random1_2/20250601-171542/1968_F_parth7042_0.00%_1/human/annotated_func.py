#State of the program right berfore the function call: stdin contains an integer t, followed by t test cases. Each test case contains two integers n and q, followed by a list of n integers, followed by q pairs of integers.
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
        
    #State: stdin is empty, t is 0, idx is 2 * t + 1, results is a list of strings containing the results of each test case, and data is a list of strings containing the remaining input lines split into substrings.
    print('\n'.join(results))
    #This is printed: results of each test case, one result per line (where results are the strings stored in the results list)

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the results. It expects the input to contain an integer t, followed by t test cases. Each test case consists of two integers n and q, a list of n integers, and q pairs of integers. The function processes each test case by calculating the XOR prefix sum of the list of integers and storing the indices of each prefix sum in a dictionary. It then answers q queries by checking if there exists a subarray within the given range that has a XOR sum equal to a given value. The function prints the results of each test case, one result per line, with 'YES' indicating the existence of such a subarray and 'NO' otherwise.

