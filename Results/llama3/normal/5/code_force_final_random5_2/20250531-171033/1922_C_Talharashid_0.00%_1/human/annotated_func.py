#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four inputs: first an integer, then a list of distinct non-decreasing integers, then an integer, and then a list of pairs of distinct integers.
    t = int(input())
    for i in range(t):
        d1 = defaultdict(int)
        
        d2 = defaultdict(int)
        
        n = int(input())
        
        lst = list(map(int, input().split()))
        
        start = 0
        
        end = len(lst) - 1
        
        inc = 1
        
        s = 0
        
        while start != end:
            mini = 11111111
            if start + 1 < len(lst):
                mini = min(abs(lst[start] - lst[start + 1]), mini)
            if start - 1 > -1:
                mini = min(abs(lst[start] - lst[start - 1]), mini)
            if mini == abs(lst[start] - lst[start + inc]):
                s += 1
            else:
                s += abs(lst[start] - lst[start + inc])
            start += inc
            d1[start] = s
        
        start = len(lst) - 1
        
        end = 0
        
        inc = -1
        
        s = 0
        
        while start != end:
            mini = 11111111
            if start + 1 < len(lst):
                mini = min(abs(lst[start] - lst[start + 1]), mini)
            if start - 1 > -1:
                mini = min(abs(lst[start] - lst[start - 1]), mini)
            if mini == abs(lst[start] - lst[start + inc]):
                s += 1
            else:
                s += abs(lst[start] - lst[start + inc])
            start += inc
            d2[start] = s
        
        m = int(input())
        
        for i in range(m):
            start, end = map(int, input().split())
            start -= 1
            end -= 1
            s = 0
            if start < end:
                s1 = abs(d1[end] - d1[start])
                s2 = abs(d2[start] - d2[end])
            else:
                s1 = abs(d2[end] - d2[start])
                s2 = abs(d1[start] - d1[end])
            print(min(s1, s2))
        
    #State: t is an integer greater than or equal to 0, i is equal to t, d1 is a dictionary with key-value pairs where the keys are the indices of lst and the values are the cumulative sum of the absolute differences between consecutive elements in lst, d2 is a dictionary with key-value pairs where the keys are the indices of lst and the values are the sum of the absolute difference between lst[start] and lst[start + inc] and the previous value of s, n is an integer, lst is a non-empty list of integers with at least 2 elements, end is the first index of lst, inc is -1, m is an integer greater than or equal to 0, start is equal to end, mini is the minimum of the absolute difference between lst[start] and lst[start - 1] and 11111111 if start - 1 is less than the length of lst. Otherwise, mini remains 11111111. If start - 1 is greater than -1, then mini is updated to be the minimum of the absolute difference between lst[start] and lst[start - 1] and 11111111. Otherwise, mini remains 11111111. If mini is equal to the absolute difference between lst[start] and lst[start + inc], then s is the sum of the absolute difference between lst[start] and lst[start - 1] and the previous value of s plus 1. Otherwise, s is the sum of the absolute difference between lst[start] and lst[start - 1] and the previous value of s plus the absolute difference between lst[start] and lst[start + inc]. If the current value of start is less than the current value of end, then s1 is the absolute difference between d1[end] and d1[start], and s2 is the absolute difference between d2[start] and d2[end]. Otherwise, s1 is the absolute difference between d2[end] and d2[start], and s2 is the absolute difference between d1[start] and d1[end], and the minimum of s1 and s2 is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer, a list of distinct non-decreasing integers, another integer, and a list of pairs of distinct integers. For each test case, it calculates the cumulative sum of absolute differences between consecutive elements in the list in both forward and backward directions, and then prints the minimum of these sums for each pair of indices in the list.

