#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of an integer n (2 <= n <= 50) followed by n space-separated integers a_1, a_2, ..., a_n (0 <= a_i <= 1).
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = ''.join(input('').split())
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: The number of zeros between the first and last occurrence of 1 in each test case is printed to the console, and the value of `t` remains unchanged.

#Overall this is what the function does:Reads a series of test cases from standard input, where each test case contains a sequence of binary digits, and prints the number of zeros between the first and last occurrence of 1 in each sequence.

