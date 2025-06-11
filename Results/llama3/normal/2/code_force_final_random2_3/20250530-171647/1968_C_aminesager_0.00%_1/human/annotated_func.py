#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains a single integer n (2 <= n <= 500). The second line contains n-1 integers x_2, x_3, ..., x_n (1 <= x_i <= 500).
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
        
    #State: t is 0, n is an integer, T is a list of n integers, a is a list containing n elements: (1000 - T[0] - T[1] - ... - T[n-2]) - T[n-1], (1000 - T[0] - T[1] - ... - T[n-2]), ..., 1000 - T[0], 1000, result is a string of space-separated integers representing the reversed list a, stdin contains no test cases, and the result which is a string of space-separated integers representing the reversed list a is being printed.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of a single integer n followed by n-1 integers. It then calculates a list of n integers by subtracting the input integers from 1000 in reverse order, and prints the resulting list in reverse order as a string of space-separated integers. The function continues this process until all test cases have been read from standard input.

