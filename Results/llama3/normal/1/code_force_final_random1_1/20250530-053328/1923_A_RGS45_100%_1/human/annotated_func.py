#State of the program right berfore the function call: stdin contains t test cases. Each test case consists of two lines: the first line contains an integer n, and the second line contains n space-separated integers. n is an integer such that 2 <= n <= 50. The second line integers are either 0 or 1, and at least one of them is 1.
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = ''.join(input('').split())
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: t is 0, _ is t, stdin contains 0 test cases, n is an integer such that 2 <= n <= 50, arr is a string of n characters, x is an integer equal to the index of the first '1' in arr, y is an integer equal to the index of the first '1' in the reverse of arr, z is a substring of arr starting at index x and ending at index n-y-1, and the number of '0's in the substring z of arr which is equal to z.count('0') has been printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a string of n binary digits (0s and 1s). It then finds the first and last occurrences of the digit '1' in the string, extracts the substring between these two occurrences, and prints the number of '0's in this substring. The function processes all test cases and prints the results for each case.

