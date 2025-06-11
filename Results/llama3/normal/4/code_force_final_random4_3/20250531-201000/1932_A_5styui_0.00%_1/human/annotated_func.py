#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case contains an integer n (1 <= n <= 50) followed by a string of n characters consisting of '.', '@', and '*' characters.
    a = int(input())
    s = 0
    for i in range(a):
        d = int(input())
        
        b = input()
        
        for j in range(len(b)):
            if b[j] == '@':
                s = s + 1
            elif b[j] == '*':
                if b[:]:
                    break
                elif b[j + 1] == '*':
                    break
        
        print(s)
        
        s = 0
        
    #State: t is at least 2, a is greater than 0, i is equal to a, d is an integer equal to the input value, b is a string equal to the input string, j is equal to the length of b, s is 0, and stdin contains t-a-1 test cases.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a string of n characters. It then counts the number of '@' characters in each string and prints the count. The function repeats this process for all test cases, ignoring '*' characters and any characters that follow them in the string. After processing all test cases, the function leaves the input stream with t-a-1 test cases remaining, where t is the initial number of test cases and a is the number of test cases processed.

