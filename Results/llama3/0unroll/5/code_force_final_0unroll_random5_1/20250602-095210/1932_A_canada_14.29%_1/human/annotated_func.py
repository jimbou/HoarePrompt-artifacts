#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case contains an integer n (1 <= n <= 50) followed by a string of n characters consisting of '.', '@', and '*' characters, where the first character is '.'.
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
        
    #State: The output state will contain the number of '@' characters in each test case string, minus the number of '*' characters that appear before the first '@' character, minus 1 if there are two '*' characters in a row. The output will be a series of integers, one for each test case.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and outputs the number of '@' characters in each test case string, adjusted by the presence of '*' characters. For each test case, it reads an integer n and a string of n characters, then counts the '@' characters while considering the '*' characters. If two '*' characters appear in a row, the count is terminated. The function prints the adjusted count for each test case.

