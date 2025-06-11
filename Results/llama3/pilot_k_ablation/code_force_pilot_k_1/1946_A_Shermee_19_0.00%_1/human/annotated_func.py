#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (1 <= n <= 10^5). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
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
        
    #State: `t` is 0, `stdin` is empty, `n`, `a`, `median_index`, `median`, `operations`, `_`, and `i` are undefined.

#Overall this is what the function does:This function reads multiple test cases from standard input, calculates the minimum number of operations required to make all numbers in each test case greater than or equal to the median, and prints the result for each test case. It consumes all input from standard input and leaves it empty.

