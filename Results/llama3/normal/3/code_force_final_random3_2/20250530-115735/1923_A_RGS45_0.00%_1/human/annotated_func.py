#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of two lines: the first line contains an integer n (2 <= n <= 50), and the second line contains n integers a_1, a_2, ..., a_n (0 <= a_i <= 1) separated by spaces.
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = str(input(''))
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: t is an integer between 1 and 1000 (inclusive), stdin contains 0 test cases, _ is t-1, n is an integer, arr is a string, x is an integer, y is an integer, z is a substring of arr, and the number of occurrences of '0' in the substring z has been printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a string of n binary digits. It then finds the first and last occurrences of the digit '1' in the string, extracts the substring between these two occurrences, and prints the number of zeros in this substring. The function repeats this process for all test cases, and does not return any value.

