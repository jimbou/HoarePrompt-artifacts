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
        
    #State: `t` is 0, `n` is undefined, `a` is undefined, `median_index` is undefined, `median` is undefined, `operations` is undefined, `stdin` is empty, `i` is undefined.

#Overall this is what the function does:Calculates and prints the minimum number of operations required to make all elements in a list of integers greater than or equal to the median, for multiple test cases.

