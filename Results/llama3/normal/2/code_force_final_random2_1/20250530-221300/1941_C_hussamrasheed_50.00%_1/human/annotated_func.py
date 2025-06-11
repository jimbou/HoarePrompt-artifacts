#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n (1 <= n <= 10^6) and then a string s of length n consisting of lowercase Latin letters.
    t = int(input())
    for i in range(t):
        n = int(input())
        
        s = input()
        
        m = s.count('map')
        
        s = s.replace('map', '')
        
        p = s.count('pie')
        
        print(m + p)
        
    #State: t is an integer greater than or equal to 0, i is t-1, n is an integer, s is a string without 'map' and 'pie', m is the number of occurrences of 'map' in the original string, p is the number of occurrences of 'pie' in the string without 'map', stdin contains 0 test cases, and the sum of the number of occurrences of 'map' and 'pie' which is m+p is being printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n and a string s. It then counts the occurrences of the substrings 'map' and 'pie' in the string, removes these substrings from the string, and prints the total count of 'map' and 'pie' occurrences. The function processes all test cases and outputs the total count for each case, leaving the input string without 'map' and 'pie' substrings.

