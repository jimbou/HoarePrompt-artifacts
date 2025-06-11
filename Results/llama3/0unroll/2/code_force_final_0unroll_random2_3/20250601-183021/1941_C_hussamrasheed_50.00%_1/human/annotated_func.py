#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n and then a string s of length n. 1 <= t <= 10^4 and 1 <= n <= 10^6. The sum of n over all test cases does not exceed 10^6.
    t = int(input())
    for i in range(t):
        n = int(input())
        
        s = input()
        
        m = s.count('map')
        
        s = s.replace('map', '')
        
        p = s.count('pie')
        
        print(m + p)
        
    #State: t is an integer between 1 and 10^4, stdin is empty.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a string s of length n. It then counts the occurrences of the substrings 'map' and 'pie' in the string s, prints their sum, and repeats this process for all test cases. The function does not modify the input variables or have any side effects beyond printing the results.

