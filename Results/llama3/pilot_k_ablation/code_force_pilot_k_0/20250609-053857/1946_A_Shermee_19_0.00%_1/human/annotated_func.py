#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines of input. The first line contains a single integer n (1 <= n <= 10^5). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
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
        
    #State: Output State: The loop has executed `t` times, and for each test case, it has calculated the median of the input list `a` and the total number of operations required to make all elements in `a` equal to the median. The total number of operations for each test case has been printed to the console. The value of `t` has been decremented to 0, and the input buffer has been exhausted.

#Overall this is what the function does:Calculates and prints the total number of operations required to make all elements in a list equal to the median for multiple test cases.

