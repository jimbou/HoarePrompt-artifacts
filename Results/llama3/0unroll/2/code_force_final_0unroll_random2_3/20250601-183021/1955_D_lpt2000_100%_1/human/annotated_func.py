#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of three lines. The first line contains three integers: n, m, and k, where 1 <= k <= m <= n <= 2 * 10^5. The second line contains n integers a_1, a_2, ..., a_n, where 1 <= a_i <= 10^6. The third line contains m integers b_1, b_2, ..., b_m, where 1 <= b_i <= 10^6.
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
        
    #State: Output State: The output state after the loop executes all the iterations is a series of integers, each representing the number of times a certain condition is met for each test case. The condition is that the number of pairs of elements that are common to both lists `aa` and `bb` is greater than or equal to `k`. The output state is a result of the loop iterating over each test case, processing the input lists `aa` and `bb`, and counting the number of times the condition is met. The state of the other variables in the precondition, such as `nabors`, remains unchanged.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of three lines: the first line contains three integers n, m, and k, and the second and third lines contain lists of integers aa and bb, respectively. The function calculates the number of times the number of pairs of common elements between aa and bb is greater than or equal to k, and prints this count for each test case.

