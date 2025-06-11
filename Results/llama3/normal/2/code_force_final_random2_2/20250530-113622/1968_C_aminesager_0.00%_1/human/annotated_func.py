#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^4). Each of the following t lines contains a single integer n (2 <= n <= 500). Each of the following t lines contains n-1 integers x_2, ..., x_n (1 <= x_i <= 500).
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
        
    #State: t is 0, n is an integer greater than 1, T is a list of n-1 integers between 1 and 500, a is a list containing n integers in reverse order, the first integer is the last element of the original list a, and the rest of the integers are the result of subtracting the corresponding element in T from the previous element in the original list a, result is a string containing all elements of the list a in reverse order, separated by spaces, i is n-1, stdin contains 0 lines of input, and the string result containing all elements of the list a in reverse order, separated by spaces is being printed.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the result. It accepts no parameters and returns no value. The function reads a series of test cases, where each test case consists of an integer n followed by n-1 integers. It then calculates a list of n integers by subtracting the corresponding element in the input list from the previous element, and prints the resulting list in reverse order, separated by spaces. The function continues this process until all test cases have been processed, at which point it terminates.

