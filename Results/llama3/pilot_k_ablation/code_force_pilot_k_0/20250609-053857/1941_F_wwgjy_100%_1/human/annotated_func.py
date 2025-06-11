#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of four lines. The first line contains three integers n, m, and k. The second line contains n integers a_1, a_2, a_3, \dots a_n. The third line contains m integers d_1, d_2, d_3, \dots d_m. The fourth line contains k integers f_1, f_2, f_3, \dots f_k. All integers are non-negative and within the given constraints.
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
        
    #State: The output state after the loop executes all the iterations is a list of integers, where each integer represents the minimum distance between the start and end points of a gap in the array 'a', and the sum of an element from array 'b' and an element from array 'f', such that the sum is within the gap and the distance is minimized. If no such sum is found within a gap, the size of the gap is printed instead.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of four lines of integers. It then calculates and prints the minimum distance between the start and end points of a gap in the first line of integers and the sum of an integer from the second line and an integer from the third line, such that the sum is within the gap. If no such sum is found within a gap, it prints the size of the gap instead. The function repeats this process for all test cases and outputs a list of integers, each representing the minimum distance or gap size for a test case.

