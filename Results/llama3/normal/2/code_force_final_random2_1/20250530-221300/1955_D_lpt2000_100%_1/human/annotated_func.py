#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three lines. The first line contains three integers: n, m, and k, where 1 <= k <= m <= n <= 2 * 10^5. The second line contains n integers a_1, a_2, ..., a_n, where 1 <= a_i <= 10^6. The third line contains m integers b_1, b_2, ..., b_m, where 1 <= b_i <= 10^6.
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
        
    #State: n is an integer, m is an integer equal to the length of aa, k is an integer, aa is a list of strings, bb is a list of strings, cnt_aa is a Counter object containing the frequency of strings in aa, cnt_bb is a Counter object containing the frequency of strings in bb, D is a Counter object containing the common elements between cnt_aa and cnt_bb, pairs_in_D is an integer representing the sum of values in D, E is a Counter object containing the elements in cnt_aa that are not in D, C is a Counter object containing the elements in cnt_bb that are not in D, fnd is 1 if pairs_in_D is greater than or equal to k, otherwise 0, nabors is 0, stdin is empty, and the value of fnd is printed for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines. It then processes each test case by comparing two lists of strings (aa and bb) and counting the common elements. The function calculates the number of pairs of common elements that meet a certain condition (pairs_in_D >= k) and prints this count for each test case. The function iterates through the lists, updating the counts of common and non-common elements, and finally prints the total count of pairs that meet the condition.

