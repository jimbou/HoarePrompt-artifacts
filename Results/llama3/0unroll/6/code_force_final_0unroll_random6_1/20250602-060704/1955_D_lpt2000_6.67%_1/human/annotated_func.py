#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of three lines. The first line contains three space-separated integers: n, m, and k (1 <= k <= m <= n <= 2 * 10^5). The second line contains n space-separated integers (1 <= a_i <= 10^6). The third line contains m space-separated integers (1 <= b_i <= 10^6).
    nabors = int(input())
    for _ in range(nabors):
        n, m, k = [int(i) for i in input().split()]
        
        aa = [int(i) for i in input().split()]
        
        bb = [int(i) for i in input().split()]
        
        cnt_aa = Counter(aa[:m])
        
        cnt_bb = Counter(bb)
        
        D = cnt_aa & cnt_bb
        
        E = cnt_aa - D
        
        C = cnt_bb - D
        
        tot = sum(D.values())
        
        fnd = 1 if tot >= k else 0
        
        for in_aa, out_aa in zip(aa[m:], aa[:n - m]):
            if D[out_aa] > 0:
                if E[out_aa] > 0:
                    E[out_aa] -= 1
                else:
                    D[out_aa] -= 1
                    C[out_aa] += 1
            else:
                E[out_aa] -= 1
            if C[in_aa] > 0:
                if C[in_aa] == D[in_aa]:
                    C[in_aa] += 1
                else:
                    D[in_aa] += 1
            else:
                E[in_aa] += 1
            tot = sum(D.values())
            fnd += 1 if tot >= k else 0
        
        print(fnd)
        
    #State: Output State: The loop will have executed all the test cases from the input, and the output will be the total number of times the condition `tot >= k` was met for each test case. The value of `nabors` will be the same as the initial state, and the input will be consumed. The output will be a series of integers, each representing the total number of times the condition was met for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines: the first line contains three integers (n, m, and k), the second line contains n integers, and the third line contains m integers. It then processes each test case by maintaining a count of common elements between the two sets of integers and updates this count as it slides a window of size m over the first set of integers. The function outputs the total number of times the count of common elements is greater than or equal to k for each test case.

