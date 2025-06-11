#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of four lines. The first line contains three space-separated integers n, m, and k. The second line contains n space-separated integers a_1, a_2, a_3, ..., a_n. The third line contains m space-separated integers d_1, d_2, d_3, ..., d_m. The fourth line contains k space-separated integers f_1, f_2, f_3, ..., f_k.
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
        
    #State: The output state after the loop executes all the iterations is a list of integers, where each integer represents the minimum distance between a pair of elements in the input lists a and b, such that the sum of the pair is within the range [start, end] and the difference between the pair is less than or equal to nd. If no such pair is found, the output is the difference between the first pair of elements in the sorted list gap.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of four lines of integers. It calculates the minimum distance between a pair of elements from two lists, such that their sum falls within a specific range and their difference is less than or equal to a certain value. If no such pair is found, it outputs the difference between the first pair of elements in a sorted list of gaps. The function prints the minimum distance for each test case.

