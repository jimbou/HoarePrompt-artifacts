#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case contains an integer n (1 <= n <= 50) followed by a string of n characters, where each character is either '.', '@', or '*'.
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
        
    #State: The number of '@' characters in each string, plus the number of '*' characters that appear before the first '@' character in each string, but only if there is at most one '*' character before the first '@' character. If there are two '*' characters before the first '@' character, the loop breaks and the count is not incremented. The output is printed for each test case.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a string of characters. It then counts the number of '@' characters in each string, plus the number of '*' characters that appear before the first '@' character, but only if there is at most one '*' character before the first '@' character. If there are two '*' characters before the first '@' character, the count is not incremented. The function prints the count for each test case.

