#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four lines. The first line contains three integers n, m, and k (2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5). The second line contains n integers a_1, a_2, a_3, ..., a_n (1 <= a_i <= 2 * 10^9, a_i < a_{i+1}). The third line contains m integers d_1, d_2, d_3, ..., d_m (1 <= d_i <= 10^9). The fourth line contains k integers f_1, f_2, f_3, ..., f_k (1 <= f_i <= 10^9).
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
                s = f[j - 1] + b[i]
                if start < s < end:
                    res = min(res, max(end - s, s - start, nd))
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
        
    #State: The loop has executed all iterations, and the output state is determined by the values of the variables in the loop head and body.

#Overall this is what the function does:This function processes multiple test cases from standard input, each containing four lines of integers. It calculates the minimum maximum gap between a set of numbers (a) and the sum of two other sets of numbers (b and f), considering the second-largest gap in a as a constraint. The function prints the minimum maximum gap for each test case, or the largest gap in a if no valid sum is found.

