#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two lines. The first line contains an integer n (2 <= n <= 50). The second line contains n space-separated integers a_1, a_2, ..., a_n (0 <= a_i <= 1) such that at least one a_i is 1.
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = ''.join(input('').split())
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: t is an integer representing the number of test cases that must be 0, stdin contains 0 test cases, _ is t-1, n is an integer (2 <= n <= 50), arr is a string of n space-separated integers a_1, a_2, ..., a_n (0 <= a_i <= 1) such that at least one a_i is 1, x is an integer representing the index of the first '1' in arr, y is an integer representing the index of the first '1' from the end of arr, z is a substring of arr starting from the first '1' to the end of arr minus the index of the first '1' from the end, and the number of '0' in z has been printed t times.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a string of n binary digits. It then finds the first and last occurrence of '1' in the binary string, extracts the substring between these two occurrences, and prints the count of '0's in this substring. The function repeats this process for each test case, ultimately consuming all input and producing the desired output.

