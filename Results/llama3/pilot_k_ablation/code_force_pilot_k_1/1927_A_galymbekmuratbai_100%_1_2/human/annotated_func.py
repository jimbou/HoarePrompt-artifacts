#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 10) followed by a string s of length n consisting of 'W' and 'B' characters, with at least one 'B' character.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s = input()
        
        first_black = s.find('B')
        
        last_black = s.rfind('B')
        
        min_paint = last_black - first_black + 1
        
        print(min_paint)
        
    #State: t is an integer between 1 and 10^4, stdin is empty, _ is t, n is an integer, s is a string, first_black is an integer, last_black is an integer, min_paint is an integer, and the minimum number of paint operations required for all test cases have been printed.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n followed by a string s of length n containing 'W' and 'B' characters. It calculates the minimum number of paint operations required to paint all 'B' characters in each string, which is the difference between the indices of the first and last 'B' characters plus one. The function then prints the minimum number of paint operations required for each test case.

