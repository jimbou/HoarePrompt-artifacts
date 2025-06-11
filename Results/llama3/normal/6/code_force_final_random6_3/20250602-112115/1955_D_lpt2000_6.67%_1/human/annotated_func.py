#State of the program right berfore the function call: stdin contains a series of test cases. Each test case consists of three lines. The first line contains three integers: n, m, and k, where 1 <= k <= m <= n <= 2 * 10^5. The second line contains n integers a_1, a_2, ..., a_n, where 1 <= a_i <= 10^6. The third line contains m integers b_1, b_2, ..., b_m, where 1 <= b_i <= 10^6. The number of test cases is between 1 and 10^4.
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
        
    #State: n is an integer, m is an integer equal to 1, k is an integer, aa is a list of at least n integers, bb is a list of integers, cnt_aa is a Counter object containing the counts of all elements of aa, cnt_bb is a Counter object containing the counts of all elements of bb, D is a Counter object containing the common elements and their counts between cnt_aa and cnt_bb, E is a Counter object containing the elements and their counts in cnt_aa that are not in cnt_bb, C is a Counter object containing the elements and their counts in cnt_bb that are not in cnt_aa, tot is an integer equal to the sum of the counts of common elements between all elements of aa and bb, fnd is 1 if the total count of common elements is at least k, otherwise 0, stdin contains 0 inputs, nabors is at least equal to the initial value of nabors, in_aa is the last element in aa, out_aa is the last element in aa, and the value of fnd is printed which is 1 if the total count of common elements is at least k, otherwise 0.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three lines: the first line contains three integers (n, m, and k), the second line contains n integers (a_1 to a_n), and the third line contains m integers (b_1 to b_m). It then calculates the number of times a sliding window of size m in the list a_1 to a_n has at least k common elements with the list b_1 to b_m. The function prints the count of such occurrences for each test case.

