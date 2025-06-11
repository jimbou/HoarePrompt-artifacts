#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n (1 <= n <= 10^6) and then a string s of length n consisting of lowercase Latin letters.
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        print(x + y)
        
    #State: a is an integer equal to the last test case, s is a string equal to the last test case, x is the number of occurrences of 'map' in the last test case, y is the number of occurrences of 'pie' in the last test case, _ is t-1, stdin contains 0 test cases, and the sum of the number of occurrences of 'map' and 'pie' in the last test case, which is x + y, is being printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n and a string s of length n. For each test case, it counts the occurrences of the substrings 'map' and 'pie' in the string s and prints their sum. The function processes all test cases and then terminates, leaving the input stream empty.

