#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains a single positive integer x (1 <= x < 2^30).
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
        
    #State: t is a positive integer greater than or equal to 0, nalla is t - 1, x is a positive integer between 1 and 2^30 - 1, length is either 30 or 31, stdin contains multiple test cases minus t, i is length - 1, s is a list containing either 30 or 31 strings: each string is '1' if the bit at the corresponding position in the binary representation of x is 1, otherwise the string is '0', except for s[i] which is either '0' if s[i] was '-1' and s[i - 1] was '1', otherwise s[i] is '1' if flag is 0, otherwise s[i] is '1' if flag is 1, otherwise s[i] is '1', and either flag is 0 or s[29] is '1', and if flag is 1, the current value of s[29] is '1', and the length of s which is either 30 or 31 is being printed, and the following is printed: a list of 30 or 31 strings representing the binary representation of x, where each string is either '1' or '0' except for s[i] which is either '0' or '1' based on the conditions described above.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case is a positive integer x between 1 and 2^30 - 1. For each test case, it converts the integer to its binary representation as a list of strings, where each string is '1' if the corresponding bit is 1 and '0' otherwise. It then performs a series of transformations on the binary representation, including flipping bits and adding a new bit in certain cases. Finally, it prints the length of the transformed binary representation and the representation itself.

