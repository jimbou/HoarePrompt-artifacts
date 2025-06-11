#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 10^6) followed by a string s of length n consisting of lowercase Latin letters.
    t = int(input())
    for i in range(t):
        n = int(input())
        
        s = input()
        
        m = s.count('map')
        
        s = s.replace('map', '')
        
        p = s.count('pie')
        
        print(m + p)
        
    #State: t is an integer between 1 and 10^4, i is t-1, n is an integer equal to the input integer, s is a string with all occurrences of 'map' and 'pie' removed, m is the number of occurrences of 'map' in the original string, p is the number of occurrences of 'pie' in the original string, and the sum of the number of occurrences of 'map' and 'pie' in the original string which is m + p is being printed

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a string s. It then counts the occurrences of the substrings 'map' and 'pie' in each string, removes these substrings from the string, and prints the total count of 'map' and 'pie' occurrences. The function processes multiple test cases, with the number of test cases specified by an initial integer t.

