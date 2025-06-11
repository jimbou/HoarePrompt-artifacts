#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 10^6) followed by a string s of length n consisting of lowercase Latin letters.
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        print(x + y)
        
    #State: The output state will be the sum of the counts of 'map' and 'pie' in each string s, printed for each test case. The stdin will be empty after the loop executes all the iterations.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a string s of length n. It then counts the occurrences of the substrings 'map' and 'pie' in each string s and prints their sum for each test case. The function processes all test cases and leaves the standard input empty after execution.

