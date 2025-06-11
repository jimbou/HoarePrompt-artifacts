#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four inputs: first an integer t, then an integer n, then a list of n unique integers a_1, a_2, ..., a_n, and finally an integer m followed by m pairs of integers x_i and y_i. The integers a_1, a_2, ..., a_n are in ascending order, and for each city i, there is a unique closest city j. The integers x_i and y_i are between 1 and n (inclusive) and are not equal.
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
        
    #State: The loop has executed t times, and for each test case, it has calculated the minimum distance between each pair of cities (x_i, y_i) and printed the result. The state of the variables outside the loop remains unchanged.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains a list of unique integers representing cities and a list of pairs of cities. It calculates the minimum distance between each pair of cities and prints the result. The function iterates through the list of cities in both ascending and descending order, calculating the minimum distance between each city and its closest neighbor. It then uses these calculations to determine the minimum distance between each pair of cities. The function prints the minimum distance for each pair of cities and repeats this process for all test cases.

