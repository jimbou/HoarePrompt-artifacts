#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of an integer n (2 <= n <= 50) followed by n space-separated integers (0 <= a_i <= 1). In each test case, at least one a_i is 1.
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = ''.join(input('').split())
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: The number of zeros in the longest contiguous subarray of ones in each test case, for t test cases.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the number of zeros in the longest contiguous subarray of ones for each test case. It accepts no parameters and returns no values, only printing the results to the console. The function's purpose is to analyze the input arrays and count the zeros within the longest contiguous subarray of ones in each test case.

