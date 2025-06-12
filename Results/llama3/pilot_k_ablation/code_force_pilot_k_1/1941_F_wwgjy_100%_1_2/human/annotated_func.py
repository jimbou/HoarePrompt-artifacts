#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four lines of input. The first line contains three integers n, m, and k. The second line contains n integers a_1, a_2, a_3, \dots a_n. The third line contains m integers d_1, d_2, d_3, \dots d_m. The fourth line contains k integers f_1, f_2, f_3, \dots f_k. All integers are non-negative and within the given constraints.
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
        
    #State: `stdin` is empty, `n`, `m`, `k` are integers at least 1, `a` is a list of integers, `b` is a sorted list of integers, `f` is a sorted list of integers, `gap` is a sorted list of tuples containing the differences between consecutive elements in `a`, `start` is an integer, `end` is an integer, `mid` is an integer, `nd` is an integer, `_` is the number of test cases, `res` is either the minimum of the maximum of `end - s`, `s - start`, and `nd` for all possible values of `s` that can be formed by adding an element from `b` to an element from `f` such that `start` is less than `s` and `s` is less than `end`, or the difference between the first two consecutive elements in `a` if `res` is still `inf`, `i` is `m` times the number of test cases.

#Overall this is what the function does:This function processes multiple test cases from standard input, each containing four lines of input: three integers n, m, and k, followed by n integers, m integers, and k integers. It calculates the minimum maximum gap between the sum of an element from the m integers and an element from the k integers, and the difference between consecutive elements in the n integers, or the difference between the first two consecutive elements in the n integers if no such sum is found. The function prints the result for each test case.

