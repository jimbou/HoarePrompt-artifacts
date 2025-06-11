#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 10^4) followed by t test cases. Each test case consists of an integer n (1 ≤ n ≤ 10) followed by a string s of length n containing only 'W' and 'B' characters, with at least one 'B' character.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s = input()
        
        first_black = s.find('B')
        
        last_black = s.rfind('B')
        
        min_paint = last_black - first_black + 1
        
        print(min_paint)
        
    #State: t is an integer between 1 and 10^4, n is an integer between 1 and 10, s is a string of length n containing only 'W' and 'B' characters, first_black is the index of the first 'B' character in s, last_black is the index of the last 'B' character in s, min_paint is the number of characters between the first and last 'B' characters in s plus 1, _ is t, stdin contains 0 test cases.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a string s of length n containing 'W' and 'B' characters. It calculates the minimum number of characters that need to be painted to have all 'B' characters together in the string, which is the number of characters between the first and last 'B' characters plus 1. The function then prints this minimum number of characters for each test case.

