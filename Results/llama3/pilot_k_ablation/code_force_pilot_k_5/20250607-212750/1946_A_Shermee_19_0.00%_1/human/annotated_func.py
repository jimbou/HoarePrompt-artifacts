#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (1 ≤ n ≤ 10^5). The second line contains n integers a_1, a_2, …, a_n (1 ≤ a_i ≤ 10^9).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        median_index = n // 2
        
        median = a[median_index]
        
        operations = 0
        
        for i in range(n):
            if a[i] < median:
                operations += median - a[i]
        
        print(operations)
        
    #State: `_` is equal to `t`, `n` is an integer greater than or equal to 0, `i` is equal to `n`, `a` is a sorted list of `n` integers, `median_index` is the integer division of `n` by 2, `median` is the middle value in the sorted list `a`, `operations` is equal to the sum of `median - a[j]` for all `j` where `a[j]` is less than the median, stdin is empty, and the sum of the differences between the median and all elements in the list `a` that are less than the median is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a list of integers. It calculates the median of each list, then computes the sum of the differences between the median and all elements in the list that are less than the median. The function prints this sum for each test case, effectively measuring the total amount of increase needed to bring all elements below the median up to the median value.

