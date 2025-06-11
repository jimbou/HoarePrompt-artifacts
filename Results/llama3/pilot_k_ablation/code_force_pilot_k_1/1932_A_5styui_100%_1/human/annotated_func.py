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
        
    #State: stdin contains t-1-a test cases, a is an integer greater than or equal to 0, s is 0, i is a, d is an integer, b is a string. If a is 0, the loop does not execute and stdin contains t-1 test cases.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a string of n characters. It then counts the number of '@' characters (representing coins) in each string, but stops counting if it encounters a '*' character (representing thorns) that is not at the end of the string or is followed by another '*'. The function prints the count of coins for each test case and resets the count for the next test case. If there are no test cases (i.e., the input integer a is 0), the function does not execute the loop and leaves the input unchanged.

