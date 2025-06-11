#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case contains an integer n (1 <= n <= 50) followed by a string of n characters. The string contains only '.', '@', and '*' characters, where '.' denotes an empty cell, '@' denotes a cell with a coin, and '*' denotes a cell with thorns. The first character of the string is always '.'.
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
        
    #State: stdin is empty, t is an integer between 1 and 1000, len is an integer between 1 and 50, s is a list of characters of length len, ret is the total number of '@' characters in all strings before the first occurrence of '

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the total number of '@' characters in each string before the first occurrence of '

