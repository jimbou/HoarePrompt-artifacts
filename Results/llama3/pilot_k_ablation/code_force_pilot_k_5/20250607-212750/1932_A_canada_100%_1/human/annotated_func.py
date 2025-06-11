#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case contains an integer n (1 <= n <= 50) followed by a string of n characters, where '.' denotes an empty cell, '@' denotes a cell with a coin, and '*' denotes a cell with thorns. The first cell is always empty.
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
        
    #State: The loop has finished executing, and the value of `ret` is being printed. `len` is an integer between 1 and 1000, `s` is a list of characters that must have at least `len` characters, `ret` is the number of '@' characters in the list `s`, `thorn` is either 0 or 1 if the last character in the list `s` is not '*', and `stdin` contains 0 test cases. If the last character in the list `s` is '*', then `thorn` is either 1 or 2, and if `thorn` is 2, the program breaks out of the most internal loop or if statement.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer length and a string of characters representing cells. It then iterates through each string, counting the number of cells with coins ('@') and keeping track of the number of consecutive cells with thorns ('*'). If two consecutive cells with thorns are encountered, the function stops counting coins for that test case. Finally, the function prints the total number of coins counted for each test case.

