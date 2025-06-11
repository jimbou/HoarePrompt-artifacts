#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case contains an integer n (1 <= n <= 50) followed by a string of n characters. The string contains only '.', '@', and '*' characters, and the first character is '.'.
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
        
    #State: The output will be the number of '@' characters in each string, minus the number of '*' characters that appear after the first '@' character, up to a maximum of 2 '*' characters. The first character of each string is ignored.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a string of characters. It then processes each string, counting the number of '@' characters and ignoring the first character. If '*' characters appear after the first '@' character, it subtracts up to 2 of them from the count. The function prints the resulting count for each test case.

