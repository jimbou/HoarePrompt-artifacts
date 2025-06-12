#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of an integer n (1 <= n <= 50) followed by a string of n characters. The string contains only '.', '@', and '*' characters, where '.' denotes an empty cell, '@' denotes a cell with a coin, and '*' denotes a cell with thorns. The first character of the string is always '.'.
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
        
    #State: stdin is empty, len is 0, s is an empty list, ret is the total number of '@' characters in all test cases before the first occurrence of '

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n followed by a string of n characters. It then processes each string, counting the number of '@' characters (representing coins) that appear before the first occurrence of two '*' characters (representing thorns) in a row. The function prints the total count of '@' characters across all test cases, effectively ignoring any characters that appear after the first occurrence of two '*' characters in a row.

