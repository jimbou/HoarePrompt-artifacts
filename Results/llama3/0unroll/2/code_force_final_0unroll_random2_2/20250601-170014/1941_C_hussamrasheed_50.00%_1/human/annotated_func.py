#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n (1 <= n <= 10^6) and then a string s of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
    t = int(input())
    for i in range(t):
        n = int(input())
        
        s = input()
        
        m = s.count('map')
        
        s = s.replace('map', '')
        
        p = s.count('pie')
        
        print(m + p)
        
    #State: The output state will be the sum of the counts of 'map' and 'pie' in each test case, printed for each test case. The value of `t` will be unchanged, and the contents of stdin will be consumed.

#Overall this is what the function does:This function reads a specified number of test cases from standard input, where each test case consists of an integer n and a string s. It then counts the occurrences of the substrings 'map' and 'pie' in each string, and prints their sum for each test case. The function consumes the contents of standard input and leaves the value of the initial test case count unchanged.

