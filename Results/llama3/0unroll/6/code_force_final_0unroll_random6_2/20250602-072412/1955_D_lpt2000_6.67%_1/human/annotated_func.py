#State of the program right berfore the function call: stdin contains a number of test cases t, followed by t test cases. Each test case consists of three integers n, m, and k, followed by two lists of integers a and b of lengths n and m respectively. 1 <= t <= 10^4, 1 <= k <= m <= n <= 2 * 10^5, 1 <= a_i, b_i <= 10^6.
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
        
    #State: The output state after the loop executes all the iterations is a series of integers, each representing the number of times a subarray of length m with at least k common elements with the array b can be found in the array a, for each test case. The number of integers in the output state is equal to the value of `nabors`.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers (n, m, k) and two lists of integers (a and b) of lengths n and m respectively. It then calculates and prints the number of times a subarray of length m with at least k common elements with the array b can be found in the array a, for each test case. The function processes all test cases and outputs the results in the order they were input.

