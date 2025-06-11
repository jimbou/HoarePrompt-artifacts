#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n and then a string s of length n.
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        print(x + y)
        
    #State: a is an integer equal to the last input, s is a string equal to the last input, x is the number of occurrences of 'map' in s, y is the number of occurrences of 'pie' in s, _ is equal to the number of test cases minus 1, stdin contains 0 test cases, and the sum of the number of occurrences of 'map' and 'pie' in s is being printed.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer 'n' and a string 's' of length 'n'. It then counts the occurrences of the substrings 'map' and 'pie' in the string 's' and prints their sum. The function repeats this process for each test case until all test cases have been processed, at which point the standard input is exhausted.

