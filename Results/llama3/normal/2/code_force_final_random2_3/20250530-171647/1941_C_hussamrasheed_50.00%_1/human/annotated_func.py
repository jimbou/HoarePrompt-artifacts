#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n (1 <= n <= 10^6) and then a string s of length n consisting of lowercase Latin letters.
    t = int(input())
    for i in range(t):
        n = int(input())
        
        s = input()
        
        m = s.count('map')
        
        s = s.replace('map', '')
        
        p = s.count('pie')
        
        print(m + p)
        
    #State: t is an integer (1 <= t <= 10^6) and equals 0, i is t-1, n is an integer, s is a string with all occurrences of 'map' removed, m is the count of 'map' in the original string s, p is the count of 'pie' in the string s after removing 'map', stdin contains 0 test cases, and the sum of the count of 'map' and the count of 'pie' which is m + p is being printed.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n and a string s. It counts the occurrences of the substring 'map' in the original string s, removes all occurrences of 'map' from the string, counts the occurrences of the substring 'pie' in the modified string, and prints the sum of the counts of 'map' and 'pie'. The function processes all test cases and prints the results for each case.

