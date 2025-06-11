#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of an integer n (1 <= n <= 50) followed by a string of n characters containing '.', '@', and '*' characters.
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
        
    #State: a is greater than or equal to 0, i is equal to a, d is an integer equal to the input value, b is a string equal to the input value, stdin contains t-1-a test cases, j is equal to the length of the input string, and s is 0.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a string of n characters. It then counts the number of '@' characters in each string, ignoring any '*' characters that are followed by another '*'. The function prints the count of '@' characters for each test case and resets the count for the next test case.

