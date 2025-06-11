#State of the program right berfore the function call: stdin contains a series of test cases. Each test case consists of four parts: the first part is an integer t (1 <= t <= 10^4), the second part is an integer n (2 <= n <= 10^5), the third part is a list of n integers a_1, a_2, ..., a_n (0 <= a_1 < a_2 < ... < a_n <= 10^9), and the fourth part is a list of m queries (1 <= m <= 10^5), where each query is a pair of integers x_i and y_i (1 <= x_i, y_i <= n; x_i != y_i).
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
        
    #State: t is an integer between 1 and 10^4, t is greater than or equal to 0, i is equal to t, d1 is a dictionary with key-value pairs where the key is the index of lst and the value is the sum of the absolute differences between the current and next elements of lst starting from the start index, d2 is a dictionary with key-value pairs where the key is the index of lst and the value is the sum of the absolute differences between the elements at the current start and start - 1 indices of lst, n is an integer, lst must have at least two elements, start is an integer equal to the first input minus 1, end is an integer equal to the second input minus 1, inc is -1, s is 0, m is an integer, and stdin contains no input. If start is less than end, then s1 is the absolute difference between the sum of absolute differences from end index and start index in d1, and s2 is the absolute difference between the sum of absolute differences from start index and end index in d2. If start is not less than end, then s1 is the absolute difference between the values of d2 at end and start indices, and s2 is the absolute difference between the values of d1 at start and end indices, and the minimum of s1 and s2 is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer t, an integer n, a list of n integers, and a list of m queries. For each test case, it calculates the minimum sum of absolute differences between elements in the list for each query, and prints the result. The function processes all test cases and then terminates, leaving the standard input empty.

