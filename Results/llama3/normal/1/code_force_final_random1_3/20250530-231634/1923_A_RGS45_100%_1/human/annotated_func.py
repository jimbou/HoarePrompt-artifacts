#State of the program right berfore the function call: stdin contains t test cases. Each test case consists of two lines: the first line contains one integer n, and the second line contains n integers a_1, a_2, ..., a_n, where a_i is either 0 or 1.
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = ''.join(input('').split())
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: t is a positive integer greater than or equal to 0, _ is t - 1, n is an integer, arr is a string, x is an integer, y is an integer, z is a substring of arr, stdin contains 0 test cases, and the number of occurrences of '0' in the substring z of arr has been printed t times.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a string of n binary digits (0s and 1s). It then finds the first and last occurrences of the digit '1' in the string, extracts the substring between these two occurrences, and prints the number of '0' digits in this substring. The function repeats this process for each test case, printing the result for each case.

