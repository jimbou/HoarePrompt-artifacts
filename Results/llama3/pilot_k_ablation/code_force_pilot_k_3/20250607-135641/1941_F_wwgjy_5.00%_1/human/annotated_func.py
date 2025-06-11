#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of four lines. The first line contains three integers n, m, and k. The second line contains n distinct integers a_1, a_2, a_3, ..., a_n (1 <= a_i <= 2 * 10^9, a_i < a_{i+1}). The third line contains m integers d_1, d_2, d_3, ..., d_m (1 <= d_i <= 10^9). The fourth line contains k integers f_1, f_2, f_3, ..., f_k (1 <= f_i <= 10^9).
    for _ in range(int(input())):
        n, m, k = [*map(int, input().split())]
        
        a = [*map(int, input().split())]
        
        b = [*map(int, input().split())]
        
        f = [*map(int, input().split())]
        
        gap = [(y - x, x, y) for y, x in zip(a[1:], a)]
        
        gap.sort(reverse=True)
        
        start = gap[0][1]
        
        end = gap[0][2]
        
        mid = (start + end) // 2
        
        nd = 0 if len(gap) == 1 else gap[1][0]
        
        b.sort()
        
        f.sort()
        
        res = inf
        
        for i in range(m):
            remain = mid - b[i]
            j = bisect.bisect_left(f, remain)
            if j == k:
                continue
            else:
                s = f[j] + b[i]
                if start < s < end:
                    res = min(res, max(end - s, s - start, nd))
                if j >= 1:
                    s = f[j - 1] + b[i]
                    if start < s < end:
                        res = min(res, max(end - s, s - start, nd))
        
        if res == inf:
            print(gap[0][0])
        else:
            print(res)
        
    #State: The loop has executed for all the test cases in the input, and the output for each test case has been printed. The variables n, m, k, a, b, f, gap, start, end, mid, nd, res, i, remain, j, and _ have been reset for each test case. The value of res has been updated and printed for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of four lines: three integers n, m, and k, followed by n distinct integers, m integers, and k integers. For each test case, it calculates the minimum distance between a pair of integers from the second and third lines that fall within a specific range defined by the first two integers of the first line. If no such pair is found, it prints the difference between the first two integers of the first line. The function prints the result for each test case and resets all variables for the next test case.

