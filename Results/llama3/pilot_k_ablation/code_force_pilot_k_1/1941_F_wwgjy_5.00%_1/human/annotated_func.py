#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four lines. The first line contains three space-separated integers: n, m, and k (2 <= n <= 10^5, 1 <= m, k <= 2 * 10^5). The second line contains n space-separated integers: a_1, a_2, ..., a_n (1 <= a_i <= 2 * 10^9, a_i < a_{i+1}). The third line contains m space-separated integers: d_1, d_2, ..., d_m (1 <= d_i <= 10^9). The fourth line contains k space-separated integers: f_1, f_2, ..., f_k (1 <= f_i <= 10^9).
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
        
    #State: The program has finished processing all test cases from stdin. The variables n, m, k, a, b, f, gap, start, end, mid, nd, and res do not have specific values as they are reassigned in each iteration of the loop. The loop has printed the minimum difference between elements of a that can be achieved by adding an element from b and an element from f, or the smallest difference between elements of a if no such combination is found, for each test case.

#Overall this is what the function does:This function processes multiple test cases from standard input, each containing four lines of integers. It calculates and prints the minimum difference between elements of the first line that can be achieved by adding an element from the second line and an element from the third line, or the smallest difference between elements of the first line if no such combination is found. The function iterates through all test cases, processing each independently, and outputs the result for each case.

