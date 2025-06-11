#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers n, m, and k (1 <= k <= m <= n <= 2 * 10^5), followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^6), and then m integers b_1, b_2, ..., b_m (1 <= b_i <= 10^6). The sum of n over all test cases does not exceed 2 * 10^5, and the sum of m over all test cases does not exceed 2 * 10^5.
    nabors = int(input())
    for _ in range(nabors):
        n, m, k = [int(i) for i in input().split()]
        
        aa = [str(i) for i in input().split()]
        
        bb = [str(i) for i in input().split()]
        
        cnt_aa = Counter(aa[:m])
        
        cnt_bb = Counter(bb)
        
        D = cnt_aa & cnt_bb
        
        pairs_in_D = sum(D.values())
        
        E = cnt_aa - D
        
        C = cnt_bb - D
        
        fnd = 1 if pairs_in_D >= k else 0
        
        for in_aa, out_aa in zip(aa[m:], aa[:n - m]):
            if D[out_aa] > 0:
                if E[out_aa] > 0:
                    E[out_aa] -= 1
                else:
                    D[out_aa] -= 1
                    pairs_in_D -= 1
                    C[out_aa] += 1
            else:
                E[out_aa] -= 1
            if C[in_aa] > 0:
                D[in_aa] += 1
                pairs_in_D += 1
                C[in_aa] -= 1
            else:
                E[in_aa] += 1
            fnd += 1 if pairs_in_D >= k else 0
        
        print(fnd)
        
    #State: The loop will have executed all the iterations, and the variable `fnd` will have been printed to the console for each test case. The values of `nabors`, `n`, `m`, `k`, `aa`, `bb`, `cnt_aa`, `cnt_bb`, `D`, `E`, `C`, and `pairs_in_D` will have been updated and used in the calculations, but their final values will not be retained after the loop finishes. The state of the other variables in the precondition that are not affected by the loop head and body will remain unchanged.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains three integers (n, m, k) and two lists of integers (a and b). It then calculates the number of pairs of elements that are common to both lists and appear at least k times in the first list, and prints this count for each test case. The function does not modify the input data or retain any information after processing each test case.

