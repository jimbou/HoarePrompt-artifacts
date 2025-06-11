#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers n, m, and k (1 <= k <= m <= n <= 2 * 10^5), followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^6), and then m integers b_1, b_2, ..., b_m (1 <= b_i <= 10^6). The sum of n over all test cases does not exceed 2 * 10^5, and the sum of m over all test cases does not exceed 2 * 10^5.
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
        
    #State: n is an integer greater than m, m is an integer greater than 0, k is an integer, aa is a list of n integers, bb is a list of m integers, cnt_aa is a Counter object containing the frequency of each integer in the first m elements of aa, cnt_bb is a Counter object containing the frequency of each integer in bb, D is a Counter object containing the common elements between cnt_aa and cnt_bb, E is a Counter object containing the elements in cnt_aa that are not in D, C is a Counter object containing the elements in cnt_bb that are not in D, tot is an integer equal to the sum of the values in D, fnd is an integer equal to 1 if tot is greater than or equal to k, otherwise 0, stdin contains no test cases, in_aa is the last element of aa[m:], out_aa is the last element of aa[:n - m], and the value of fnd which is 1 if the sum of the values in D is greater than or equal to k, otherwise 0 is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three integers n, m, and k, followed by n integers a_1 to a_n, and then m integers b_1 to b_m. It then calculates the number of positions where the sum of common elements between the first m elements of a_1 to a_n and b_1 to b_m is greater than or equal to k, as the window of the first m elements of a_1 to a_n slides over the rest of the list. The function prints the count of such positions for each test case.

