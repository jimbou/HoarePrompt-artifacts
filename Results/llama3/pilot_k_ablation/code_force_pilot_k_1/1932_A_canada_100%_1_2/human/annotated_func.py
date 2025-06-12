#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of an integer n (1 <= n <= 50) followed by a string of n characters. The string contains only '.', '@', and '*' characters, where '.' denotes an empty cell, '@' denotes a cell with a coin, and '*' denotes a cell with thorns. The first character of the string is '.'.
    for _ in range(int(input())):
        len = int(input())
        
        s = list(input())
        
        ret = 0
        
        thorn = 0
        
        for i in s:
            if i == '@':
                thorn = 0
                ret += 1
            elif i == '*':
                thorn += 1
                if thorn == 2:
                    break
            else:
                thorn = 0
        
        print(ret)
        
    #State: stdin is empty, t is an integer between 1 and 1000, len is an integer between 1 and 50, s is a string of length n, ret is the sum of the number of '@' characters in each string before the first occurrence of '

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a string of n characters. The function then iterates through each string, counting the number of '@' characters (representing coins) until it encounters two '*' characters (representing thorns) in a row. The function prints the total count of '@' characters for each test case, effectively ignoring any characters after the first occurrence of two consecutive '*' characters. The function repeats this process for all test cases, leaving the standard input empty upon completion.

