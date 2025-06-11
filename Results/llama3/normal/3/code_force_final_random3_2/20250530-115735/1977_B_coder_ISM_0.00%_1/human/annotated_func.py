#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains a single positive integer x (1 ≤ x < 2^30).
    t = int(input())
    for nalla in range(t):
        x = int(input())
        
        s = []
        
        length = 30
        
        for i in range(30):
            if x & pow(2, i):
                s.append('1')
            else:
                s.append('0')
        
        print(*s)
        
        flag = 0
        
        for i in range(0, 29):
            if flag and s[i] == '0':
                s[i] = '1'
                flag = 0
            if flag == 0 and s[i] == s[i + 1] and s[i] == '1':
                s[i] = '-1'
                flag = 1
            elif flag == 1:
                s[i] = '0'
            else:
                pass
        
        if flag and s[29] == '0':
            s[29] = '1'
        elif flag:
            s[29] = '0'
            s.append('1')
            length += 1
        
        for i in range(1, length):
            if (s[i] == '-1') & (s[i - 1] == '1'):
                s[i] = '0'
                s[i - 1] = '-1'
        
        print(length)
        
        print(*s)
        
    #State: t is a positive integer greater than or equal to 0, nalla is equal to t, i is either 30 or 31, length is either 30 or 31, x is an integer, flag is either 0 or 1, and s is a list containing either 30 or 31 strings. If s[i] is '-1' and s[i - 1] is '1', then s[i] is '0' and s[i - 1] is '-1'. Otherwise, no changes are made to s[i] and s[i - 1]. The length of the list s which is either 30 or 31 is being printed, and the list s is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case is a single positive integer x. For each test case, it converts the integer into a binary string, applies a series of transformations to the binary string (including flipping bits and adding a new bit if necessary), and then prints the length of the transformed binary string and the string itself.

