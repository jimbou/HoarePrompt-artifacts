#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four lines. The first line contains three space-separated integers: n, m, and k. The second line contains n space-separated integers: a_1, a_2, ..., a_n. The third line contains m space-separated integers: d_1, d_2, ..., d_m. The fourth line contains k space-separated integers: f_1, f_2, ..., f_k.
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
        
    #State: `stdin` is empty, `n`, `m`, and `k` are the last values read from `stdin`, `a` is the last list of integers read from `stdin`, `b` is the last sorted list of integers read from `stdin`, `f` is the last sorted list of integers read from `stdin`, `gap` is the last sorted list of tuples containing the differences between consecutive elements in `a`, `start` and `end` are the last integers representing the start and end of the largest gap in `a`, `mid` is the last integer representing the middle of the largest gap in `a`, `nd` is the last integer representing the second-largest gap in `a` (or 0 if there is only one gap), `res` is the last minimum of its initial value (infinity) and the maximum of `end - s`, `s - start`, and `nd` for all `s` that are within the range of `start` and `end`, `remain` is the last integer equal to `mid` minus the last element of `b`, `j` is the last integer representing the insertion point of `remain` in `f` to maintain sorted order, `i` is the last value of `m-1`.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of four lines. It then processes each test case by finding the largest gap in the first list of integers, sorting the second and third lists, and calculating the minimum distance between the middle of the largest gap and the sum of an element from the second list and an element from the third list that falls within the largest gap. If no such sum exists, it prints the size of the largest gap. The function repeats this process for all test cases, emptying the standard input in the process.

