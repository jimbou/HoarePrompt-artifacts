#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of an integer n (1 <= n <= 50) followed by a string of n characters, where each character is either '.', '@', or '*'.
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
        
    #State: `len` is an integer greater than or equal to 0, `s` is a list of characters that must have at least `len` characters, `ret` is the total number of '@' characters in all test cases before the first occurrence of '

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the total count of '@' characters in each test case before the first occurrence of '

