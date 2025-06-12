#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four lines. The first line contains three integers n, m, and k. The second line contains n integers a_1, a_2, a_3, \dots a_n. The third line contains m integers d_1, d_2, d_3, \dots d_m. The fourth line contains k integers f_1, f_2, f_3, \dots f_k.
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
        
    #State: The program has finished processing all test cases from the standard input. The values of variables n, m, k, a, b, f, gap, start, end, mid, nd, res are undefined because they are local to the loop and are reinitialized in each iteration. The loop has printed the minimum difference between the sum of an element from list b and an element from list f that falls within the range of two consecutive elements in list a, or the difference between two consecutive elements in list a if no such sum is found, for each test case.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case contains four lines of integers. It calculates and prints the minimum difference between the sum of an element from the second list and an element from the third list that falls within the range of two consecutive elements in the first list. If no such sum is found, it prints the difference between two consecutive elements in the first list. The function iterates over all test cases, printing the result for each case.

