#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of three lines. The first line contains three space-separated integers: n, m, and k, where 1 <= k <= m <= n <= 2 * 10^5. The second line contains n space-separated integers: a_1, a_2, ..., a_n, where 1 <= a_i <= 10^6. The third line contains m space-separated integers: b_1, b_2, ..., b_m, where 1 <= b_i <= 10^6.
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
        
    #State: n is an integer greater than 0, m is an integer less than n, k is an integer, aa is a list of at least n strings, bb is a list of strings, cnt_aa is a Counter object containing the frequency of each string in aa[:m], cnt_bb is a Counter object containing the frequency of each string in bb, D is a Counter object containing the common elements between cnt_aa and cnt_bb, pairs_in_D is an integer representing the total count of common elements, E is a Counter object containing the elements in cnt_aa that are not in D, C is a Counter object containing the elements in cnt_bb that are not in D, fnd is 1 if pairs_in_D is greater than or equal to k, otherwise 1 if it was 1 before, 0 if it was 0 before, nabors is 0, stdin contains 0 inputs, in_aa is the last element in aa[m:], out_aa is the last element in aa[:n - m]. D contains all the common elements between cnt_aa and cnt_bb, pairs_in_D is the total count of common elements, E contains all the elements in cnt_aa that are not in D, C contains all the elements in cnt_bb that are not in D, fnd is 1 if pairs_in_D is greater than or equal to k, otherwise 1 if it was 1 before, 0 if it was 0 before, and the value of fnd is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines: the first line contains three integers n, m, and k, and the second and third lines contain n and m space-separated strings, respectively. It then calculates the number of pairs of strings that appear in both lists within a sliding window of size m, and prints the number of positions where the number of such pairs is greater than or equal to k. The function processes all test cases and prints the results for each case.

