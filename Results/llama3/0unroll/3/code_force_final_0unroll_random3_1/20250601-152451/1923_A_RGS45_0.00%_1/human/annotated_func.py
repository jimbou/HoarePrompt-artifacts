#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of an integer n (2 <= n <= 50) followed by n space-separated integers a_1, a_2, ..., a_n (0 <= a_i <= 1) such that at least one a_i is 1.
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = str(input(''))
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: The number of zeros between the first and last occurrence of 1 in each test case array has been printed to the console, and the input buffer has been fully consumed. The variable t has been exhausted and is no longer in the execution state.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an array of binary digits. It then identifies the first and last occurrence of the digit '1' in each array, extracts the subarray between these two occurrences, counts the number of zeros in this subarray, and prints this count to the console. The function processes all test cases and consumes the entire input buffer, leaving no remaining input or state after execution.

