#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^4). Each of the following t lines contains a single integer n (2 <= n <= 500). Each of the following t lines contains n-1 integers x_2, ..., x_n (1 <= x_i <= 500).
    t = int(input())
    while t:
        t = t - 1
        
        n = int(input())
        
        line = input('')
        
        T = list(map(int, line.split()))
        
        a = [1000]
        
        for i in range(1, n):
            a.append(a[i - 1] + T[i - 1])
        
        result = ' '.join(map(str, a))
        
        print(result)
        
    #State: t is 0, n is an integer between 2 and 500, T is a list of n-1 integers between 1 and 500, a is a list containing n integers: 1000, 1000 + T[0], 1000 + T[0] + T[1], ..., 1000 + T[0] + T[1] + ... + T[n-2], i is n-1, result is a string of space-separated integers corresponding to the elements of list a, stdin contains 0 lines of input, and a string of space-separated integers corresponding to the elements of list a is being printed.

#Overall this is what the function does:The function reads a series of input lines from stdin, where the first line contains an integer t representing the number of test cases, and each test case consists of two lines: the first line contains an integer n, and the second line contains n-1 integers. The function processes each test case by creating a list a of n integers, where the first element is 1000, and each subsequent element is the sum of the previous element and the corresponding integer from the input line. The function then prints a string of space-separated integers corresponding to the elements of list a. The function repeats this process t times, until all test cases have been processed, at which point stdin contains 0 lines of input.

