#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of an integer n (1 <= n <= 50) followed by a string of n characters, where '.' denotes an empty cell, '@' denotes a cell with a coin, and '*' denotes a cell with thorns. The first cell is always empty ('.').
    a = int(input())
    s = 0
    for i in range(a):
        d = int(input())
        
        b = input()
        
        for j in range(len(b)):
            if b[j] == '@':
                s = s + 1
            elif b[j] == '*':
                if j == len(b) - 1:
                    break
                elif b[j + 1] == '*':
                    break
        
        print(s)
        
        s = 0
        
    #State: `a` is 0, `i` is equal to the initial value of `a`, `s` is 0, `d` is the last test case integer, `b` is the last test case string, stdin is empty.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n followed by a string of n characters. It then counts the number of '@' characters (representing coins) in each string, ignoring any '*' characters (representing thorns) that are not immediately followed by another '*'. The function prints the count of coins for each test case and resets the count after each test case. After processing all test cases, the function leaves the input stream empty.

