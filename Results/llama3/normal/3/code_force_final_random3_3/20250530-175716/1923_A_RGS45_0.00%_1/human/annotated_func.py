#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two lines: the first line contains an integer n (2 <= n <= 50), and the second line contains n space-separated integers a_1, a_2, ..., a_n (0 <= a_i <= 1) where a_i = 0 means the i-th cell is free and a_i = 1 means the i-th cell contains a chip. In each test case, at least one cell contains a chip.
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = str(input(''))
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: t is an integer larger than 0 and at least t, n is an integer, arr is a string, x is an integer, y is an integer, z is a substring of arr, stdin contains 0 test cases, and the number of occurrences of '0' in the substring z of arr is being printed

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n followed by a string of n space-separated binary digits (0s and 1s). It then finds the first and last occurrences of '1' in the string, extracts the substring between these two occurrences, and prints the number of '0's in this substring. The function repeats this process for each test case, ultimately consuming all input from standard input and producing a series of output values representing the count of '0's in each substring.

