#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (2 <= n <= 2 * 10^5) followed by two strings of length n consisting of '<' and/or '>'. n is even. The sum of n over all test cases doesn't exceed 2 * 10^5.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = input()
        
        b = input()
        
        for i in range(1, n, 2):
            if i + 1 < n and a[i] == b[i + 1] == '<' or a[i] == b[i - 1] == '<':
                print('No')
                break
        else:
            print('yes')
        
    #State: The output state will be a series of 'yes' or 'no' printed to the console, one for each test case. The 'yes' indicates that the given strings do not contain any adjacent '<' characters, while 'no' indicates that such adjacent '<' characters exist. The number of 'yes' or 'no' printed will be equal to the number of test cases (t). The value of t, n, a, and b will remain unchanged.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two strings of length n. It checks if the strings contain any adjacent '<' characters and prints 'yes' if no such adjacent characters exist, and 'no' otherwise. The function processes all test cases and prints the results to the console, one for each test case.

