#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four lines of input. The first line contains three integers n, m, and k. The second line contains n integers a_1, a_2, a_3, \dots a_n. The third line contains m integers d_1, d_2, d_3, \dots d_m. The fourth line contains k integers f_1, f_2, f_3, \dots f_k.
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
        
    #State: stdin is empty, `n`, `m`, `k`, `a`, `b`, `f`, `gap`, `start`, `end`, `mid`, `nd`, `res`, `i`, `remain`, `j`, `_` are not defined.

#Overall this is what the function does:This function reads multiple test cases from standard input, each containing four lines of input: three integers n, m, and k, followed by n integers, m integers, and k integers. It then calculates the minimum maximum gap between a pair of elements from the first set of integers and the sum of an element from the second set and an element from the third set, considering the constraints imposed by the gaps between consecutive elements in the first set. The function prints the calculated minimum maximum gap for each test case. If no such gap can be found, it prints the maximum gap between consecutive elements in the first set. After processing all test cases, the function leaves the standard input empty and does not define any variables.

