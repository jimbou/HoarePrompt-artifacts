#State of the program right berfore the function call: stdin contains t+2*t lines. The first line contains one integer t (1 <= t <= 1000). Each of the following t lines contains one integer n (2 <= n <= 50). Each of the following t lines contains n integers a_1, a_2, ..., a_n (0 <= a_i <= 1) separated by spaces. In each test case, at least one cell contains a chip (a_i = 1).
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = str(input(''))
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: t is 0, n is an integer equal to the input, arr is a string equal to the input, x is an integer equal to the index of the first '1' in arr, y is an integer equal to the index of the first '1' in the reverse of arr, z is a substring of arr from index x to n - y - 1, stdin is empty, and the number of occurrences of '0' in the substring z has been printed for each test case.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the number of zeros in a specific substring for each test case. It accepts no parameters and returns no value. The function reads an integer t, representing the number of test cases, followed by t lines containing an integer n and a string of n binary digits. For each test case, it finds the first and last occurrence of '1' in the string, extracts the substring between these indices, and prints the count of zeros in this substring. The function processes all test cases and leaves the input stream empty.

