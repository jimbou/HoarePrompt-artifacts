#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of three lines. The first line contains three integers n, m, and k. The second line contains n integers a_1, a_2, ..., a_n. The third line contains m integers b_1, b_2, ..., b_m.
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
        
    #State: Output State: The loop will execute `nabors` times, and in each iteration, it will read two lines of input from stdin, process the data, and print the result. The output will be a series of integers, each representing the number of times the condition `tot >= k` is met for a given test case. The state of the variables `nabors`, `n`, `m`, `k`, `aa`, `bb`, `cnt_aa`, `cnt_bb`, `D`, `E`, `C`, `tot`, and `fnd` will be updated accordingly in each iteration, but their values will not be retained across iterations. The final output state will be the last printed integer, and the values of all variables will be lost after the loop finishes executing.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines: the first line contains three integers n, m, and k, the second line contains n integers, and the third line contains m integers. It then processes each test case by counting the occurrences of each integer in the two sets of numbers, calculates the total count of common integers, and checks how many times the total count is greater than or equal to k. The function prints the result for each test case, which is the number of times the condition is met.

