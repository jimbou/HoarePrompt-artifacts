#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three lines. The first line contains three integers: n, m, and k (1 <= k <= m <= n <= 2 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^6). The third line contains m integers b_1, b_2, ..., b_m (1 <= b_i <= 10^6).
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
        
    #State: Output State: The loop will execute `nabors` times, and in each iteration, it will read two lines of input from stdin, process the data, and print the result. After all iterations, the output state will be the cumulative result of all the iterations, which is the total number of times the condition `pairs_in_D >= k` is true for all test cases. The value of `nabors` will remain unchanged, as it is not modified within the loop.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines: the first line contains three integers (n, m, and k), the second line contains n integers, and the third line contains m integers. It then processes each test case by counting the occurrences of integers in the second and third lines, and calculates the number of times a certain condition (pairs_in_D >= k) is true. The function prints the cumulative result of this calculation for all test cases.

