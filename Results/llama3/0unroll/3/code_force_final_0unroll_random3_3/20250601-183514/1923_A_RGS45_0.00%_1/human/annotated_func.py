#State of the program right berfore the function call: stdin contains t+2*t lines. The first line contains an integer t (1 <= t <= 1000). Each of the following t blocks of two lines contains an integer n (2 <= n <= 50) and a list of n space-separated integers (0 <= a_i <= 1) respectively.
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = str(input(''))
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: The output state will contain t number of lines, each containing the count of zeros in the subarray of the input array that starts from the first occurrence of '1' and ends at the last occurrence of '1'. The input array is a list of n space-separated integers (0 <= a_i <= 1) and 1 <= n <= 50. The value of t is an integer between 1 and 1000.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the count of zeros in a subarray of the input array. The subarray starts from the first occurrence of '1' and ends at the last occurrence of '1'. The function processes multiple test cases, where each test case consists of an integer n and a list of n space-separated integers. The function prints the count of zeros for each test case.

