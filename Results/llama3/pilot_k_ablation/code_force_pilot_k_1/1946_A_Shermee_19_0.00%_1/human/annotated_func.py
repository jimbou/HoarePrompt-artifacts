#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (the length of the array) and then a space-separated list of integers. The length of the list is equal to the first integer. All integers are between 1 and 10^9.
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
        
    #State: `t` is 0, `stdin` is empty, `n` is not defined, `a` is not defined, `median_index` is not defined, `median` is not defined, `operations` is not defined.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer length and a list of integers. It calculates the median of each list, counts the number of operations required to make all elements in the list greater than or equal to the median, and prints the total operations for each test case. After processing all test cases, the function leaves the standard input empty and does not return any value.

