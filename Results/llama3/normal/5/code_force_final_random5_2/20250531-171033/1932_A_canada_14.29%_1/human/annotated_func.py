#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case contains an integer n (1 <= n <= 50) followed by a string of n characters consisting of '.', '@', and '*' characters.
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
        
    #State: ret is an integer greater than or equal to 0, thorn is 0, len is an integer greater than or equal to 0, s is a list of characters, stdin is empty, and the value of ret which is an integer greater than or equal to 0 is being printed

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n followed by a string of n characters. It then processes each string, counting the number of '@' characters that are not preceded by two '*' characters. The function prints the count of such '@' characters for each test case.

