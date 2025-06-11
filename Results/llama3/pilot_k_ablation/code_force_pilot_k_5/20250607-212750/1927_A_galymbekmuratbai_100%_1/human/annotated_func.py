#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 10) followed by a string s of length n consisting of 'W' and 'B' characters, with at least one 'B' character.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s = input()
        
        first_black = s.find('B')
        
        last_black = s.rfind('B')
        
        min_paint = last_black - first_black + 1
        
        print(min_paint)
        
    #State: t is an integer equal to 0, n is an integer between 1 and 10, s is a string of length n consisting of 'W' and 'B' characters, first_black is an integer equal to the index of the first 'B' character in s, last_black is an integer equal to the index of the last 'B' character in s, min_paint is an integer equal to the number of 'B' characters in s, stdin contains 0 test cases, _ is equal to t, and the minimum number of 'B' characters in s which is min_paint has been printed for all test cases.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a string s of length n containing 'W' and 'B' characters. It calculates the minimum number of 'B' characters in each string, which is the difference between the indices of the last and first 'B' characters plus one, and prints this value for each test case. The function processes all test cases and then terminates, leaving the input stream empty.

