#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of four lines. The first line contains three space-separated integers: n, m, and k. The second line contains n space-separated integers. The third line contains m space-separated integers. The fourth line contains k space-separated integers.
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
        
    #State: The program prints either the first element of the first tuple in the gap list if the minimum value of the maximum differences between end and start, start and s, and nd is infinity, or the minimum value of the maximum differences between end and start, start and s, and nd if it is not infinity.

#Overall this is what the function does:The function processes multiple test cases from standard input, where each test case consists of four lines of integers. It calculates the minimum value of the maximum differences between two points (start and end) and a third point (s), considering a gap size (nd) if available. If no such value is found, it prints the initial gap size; otherwise, it prints the minimum value of the maximum differences.

