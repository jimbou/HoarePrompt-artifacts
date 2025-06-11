#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 10^6) followed by a string s of length n consisting of lowercase Latin letters.
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        print(x + y)
        
    #State: a is an integer equal to the first input, s is a string equal to the second input, x is the count of 'map' in s, y is the count of 'pie' in s, _ is t-1, t is greater than or equal to 0, stdin contains 0 test cases, and the sum of the count of 'map' and 'pie' in s which is x + y is being printed

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a string s of length n. It then counts the occurrences of the substrings 'map' and 'pie' in each string s and prints their sum. The function processes all test cases and prints the sum of 'map' and 'pie' counts for each case.

