#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of an integer n (1 <= n <= 50) followed by a string of n characters, where '.' denotes an empty cell, '@' denotes a cell with a coin, and '*' denotes a cell with thorns. The first cell is always empty ('.').
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
                thorn == 0
        
        print(ret)
        
    #State: len is an integer between 1 and 1000, s is a list of characters that must have at least len characters, ret is the number of '@' characters in the list s, thorn is 0 if the last character in s is not '*', otherwise thorn is the number of '*' characters in the list s that are not followed by another '*', stdin contains 0 test cases, _ is t-1, input() must be greater than or equal to 0, and the number of '@' characters in the list s which is ret is being printed

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer length followed by a string of that length. The string contains three types of characters: '.' (empty cell), '@' (cell with a coin), and '*' (cell with thorns). The function counts the number of '@' characters in each string, but stops counting if it encounters two '*' characters in a row. The function then prints the count of '@' characters for each test case.

