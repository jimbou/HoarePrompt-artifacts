#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 2 <= n <= 10^5, a is a list of n integers where 0 <= a_1 < a_2 < ... < a_n <= 10^9, m is an integer such that 1 <= m <= 10^5, and for each of the m queries, x and y are integers such that 1 <= x, y <= n and x != y. The sum of n over all test cases does not exceed 10^5, and the sum of m over all test cases does not exceed 10^5. For every city, the closest city is determined uniquely.
def func():
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
        
    #State: After processing all test cases and their respective queries, the output state will be a series of printed distances corresponding to each query. Since the state of the variables `t`, `n`, `lst`, `m`, and the queries themselves is not modified within the loop, the output state can be described as the printed results of the queries.
    #
    #Output State:
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of city coordinates and a series of queries. For each query, it calculates and prints the minimum distance from one city to the closest other city, excluding a specified city.

