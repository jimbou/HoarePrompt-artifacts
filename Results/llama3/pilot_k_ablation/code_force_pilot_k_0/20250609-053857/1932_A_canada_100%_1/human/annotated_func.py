#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of an integer n (1 <= n <= 50) followed by a string of n characters containing only '.', '@', and '*'.
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
        
    #State: The number of '@' characters in each test case string, plus the number of '*' characters that appear before the second '@' character in each string, assuming that the input string contains at least two '@' characters. If the string contains less than two '@' characters, the output will be the number of '@' characters in the string.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the count of '@' characters plus the count of '*' characters before the second '@' character in each test case string. If a string contains less than two '@' characters, it prints the count of '@' characters.

