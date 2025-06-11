#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 10) followed by a string s of length n consisting of 'W' and 'B' characters, with at least one 'B' character.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s = input()
        
        first_black = s.find('B')
        
        last_black = s.rfind('B')
        
        min_paint = last_black - first_black + 1
        
        print(min_paint)
        
    #State: t is 0, stdin is empty, n is an integer between 1 and 10, s is a string of length n consisting of 'W' and 'B' characters, with at least one 'B' character, first_black is the index of the first 'B' in s, last_black is the index of the last 'B' in s, min_paint is the number of 'B' characters in s plus the number of 'W' characters between the first and last 'B' characters, and the minimum number of paint operations required to paint the string s, which is the sum of the number of 'B' characters and the number of 'W' characters between the first and last 'B' characters, is printed for each test case.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a string of 'W' and 'B' characters. It calculates and prints the minimum number of paint operations required to paint the string, which is the sum of the number of 'B' characters and the number of 'W' characters between the first and last 'B' characters. The function processes all test cases and then terminates, leaving the standard input empty.

