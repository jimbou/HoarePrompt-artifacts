#State of the program right berfore the function call: stdin contains multiple lines of input: the first line contains an integer (number of test cases), and each subsequent test case consists of two lines - the first line contains an integer (length of the strip), and the second line contains a string of 'W's and 'B's (representing white and black cells respectively) of the same length as the integer in the first line.
    ma = mi = 0
    m = int(input())
    s = input()
    c = d = 0
    l = []
    for j in s:
        c += 1
        
        if j == 'B':
            mi = c
            break
        
    #State: `m` is an integer, `s` is a string of 'W's and 'B's that must have at least `len(s)` characters, `ma` is 0, `mi` is the index of the first 'B' in `s` if 'B' exists in `s`, otherwise `mi` is 0, `c` is `len(s)`, `d` is 0, `l` is an empty list, `j` is the last character in the string `s`, stdin contains multiple lines of input: each test case consists of two lines - the first line contains an integer (length of the strip), and the second line contains a string of 'W's and 'B's (representing white and black cells respectively) of the same length as the integer in the first line.
    for j in s[::-1]:
        d += 1
        
        if j == 'B':
            ma = len(s) - d
            break
        
    #State: `m` is an integer, `s` is a string of 'W's and 'B's that must have at least `len(s)` characters, `ma` is `len(s) - d` if 'B' exists in `s`, otherwise `ma` is 0, `mi` is the index of the first 'B' in `s` if 'B' exists in `s`, otherwise `mi` is 0, `c` is `len(s)`, `d` is `len(s)`, `l` is an empty list, `j` is the first character in the string `s`.
    return ma - mi + 2
    #The program returns the difference between the length of the string `s` minus the distance `d` and the index of the first 'B' in `s` plus 2, but only if 'B' exists in `s`, otherwise it returns 2.

#Overall this is what the function does:This function calculates the length of the shortest sub-strip of a given strip of white ('W') and black ('B') cells that contains at least one black cell. If the strip contains at least one black cell, the function returns the length of the shortest sub-strip; otherwise, it returns 2. The function takes no arguments and reads input from standard input, expecting multiple test cases where each test case consists of two lines: the first line contains the length of the strip, and the second line contains the strip itself.

