#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 <= n <= 10^5) and then a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
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
        
    #State: t is a positive integer greater than or equal to 0, _ is t, n is an integer, a is a sorted list of integers, median_index is an integer, median is an integer, i is n, operations is increased by the sum of positive integers (median - a[j]) for all j where a[j] is less than median, and the value of operations which is the sum of positive integers (median - a[j]) for all j where a[j] is less than median is being printed, and stdin contains no input.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a list of n integers. It calculates the median of the list, then computes the sum of the differences between the median and all numbers less than the median. The function prints this sum for each test case, effectively calculating the minimum number of operations required to make all numbers in the list greater than or equal to the median.

