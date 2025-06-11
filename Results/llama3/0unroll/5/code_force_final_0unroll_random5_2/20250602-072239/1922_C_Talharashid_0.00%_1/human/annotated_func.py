#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four inputs: first an integer, then a list of unique non-decreasing integers, then an integer, and then a list of pairs of integers. The first integer is the number of cities, the list of integers represents the coordinates of the cities, the second integer is the number of queries, and the list of pairs of integers represents the queries, where each pair contains two different city indices.
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
        
    #State: The loop has executed all the iterations and the output state is the result of the last iteration. The values of the variables in the loop head and body have been updated accordingly. The state of the other variables in the precondition that are not affected by the loop head and body remains unchanged.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains a number of cities, their coordinates, a number of queries, and query pairs of city indices. For each query, it calculates the minimum distance between the two cities by considering two paths: one in ascending order of city coordinates and one in descending order. The function then prints the minimum distance for each query.

