#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains a single integer n (2 <= n <= 500). The second line contains n-1 integers x_2,...,x_n (1 <= x_i <= 500). The number of test cases does not exceed 10^4 and the sum of values n over all test cases does not exceed 2 * 10^5.
    t = int(input())
    while t:
        t = t - 1
        
        n = int(input())
        
        line = input('')
        
        T = list(map(int, line.split()))
        
        a = [1000]
        
        for i in range(1, n):
            a.append(a[i - 1] - T[i - 1])
        
        a = a[::-1]
        
        result = ' '.join(map(str, a))
        
        print(result)
        
    #State: The output state is a list of integers, where each integer represents the difference between the previous integer and the corresponding value in the input list T, in reverse order. The first integer in the list is 1000.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer n and a list of n-1 integers. It then calculates a new list of integers by subtracting each value in the input list from the previous value, starting from 1000, and prints the resulting list in reverse order. The function repeats this process for each test case.

