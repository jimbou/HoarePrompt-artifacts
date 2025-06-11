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
        
    #State: a is at least a, i is a - 1, d is an integer between 1 and 50, b is a string of d characters where '.' denotes an empty cell, '@' denotes a cell with a coin, and '*' denotes a cell with thorns, and the first cell is always empty ('.'), j is equal to the length of string b, s is 0, and stdin is empty, and the total number of coins in string b which is s is being printed

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a string of n characters. It then counts the number of coins ('@') in each string, ignoring any strings that contain thorns ('*') after the first coin, and prints the total number of coins for each test case. The function repeats this process for all test cases provided in the input.

