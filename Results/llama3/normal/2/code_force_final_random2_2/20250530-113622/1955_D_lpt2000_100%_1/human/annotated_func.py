#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains three integers n, m, and k (1 <= k <= m <= n <= 2 * 10^5) followed by two lists of integers a and b of lengths n and m respectively, where 1 <= a_i, b_i <= 10^6.
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
        
    #State: n is an integer between 1 and 2 * 10^5, m is an integer between 1 and n, k is an integer between 1 and m, aa is a list of strings of length n, bb is a list of strings of length m, cnt_aa is a Counter object containing the frequency of each string in aa[:m], cnt_bb is a Counter object containing the frequency of each string in bb, D is a Counter object containing the common elements between cnt_aa and cnt_bb, pairs_in_D is an integer representing the total count of common elements, E is a Counter object containing the elements in cnt_aa that are not in D, C is a Counter object containing the elements in cnt_bb that are not in D, fnd is 1 if pairs_in_D is greater than or equal to k, otherwise 0, _ is nabors - 1, nabors is an integer between 1 and 10^4 (inclusive), stdin contains 0 test cases, in_aa is the first element in aa[m:], out_aa is the first element in aa[:n - m], and this is printed: fnd which is 1 if pairs_in_D is greater than or equal to k, otherwise 0.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the number of times a certain condition is met. For each test case, it reads three integers (n, m, k) and two lists of integers (aa and bb) of lengths n and m, respectively. It then calculates the common elements between the first m elements of aa and bb, and checks if the count of these common elements is greater than or equal to k. The function slides a window of size m over the list aa, updating the count of common elements and printing the number of times the condition is met.

