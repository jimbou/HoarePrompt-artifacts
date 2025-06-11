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
                thorn = 0
        
        print(ret)
        
    #State: `len` is an integer, `s` is a list of characters, `ret` is an integer, `thorn` is 0 or 1, `stdin` contains 0 test cases, and the value of `ret` is being printed.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer length and a string of characters. It then processes each string, counting the number of '@' characters that are not preceded by two '*' characters. The count is printed for each test case. The function does not modify the input strings or lengths, and it does not retain any information between test cases. After processing all test cases, the function terminates, leaving the input stream empty.

