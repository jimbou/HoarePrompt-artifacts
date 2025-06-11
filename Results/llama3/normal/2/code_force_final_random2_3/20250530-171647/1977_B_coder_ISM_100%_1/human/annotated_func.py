#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t positive integers x (1 <= x < 2^30).
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
        
    #State: t is an integer between 0 and 10^4 (inclusive), x is an integer, nalla is t, stdin contains no positive integers, i is 30, the list s contains either 30 or 31 elements. If s[i] is '-1' and s[i - 1] is '1', then the value of s[i] is '0' and the value of s[i - 1] is '-1'. Otherwise, the values of s, flag, t, x, nalla, stdin, and length remain unchanged. Additionally, either flag is 0 or s[29] is '1', and the length of the list s which is either 30 or 31 is being printed, and the elements of the list s are being printed

#Overall this is what the function does:This function reads a series of positive integers from standard input, modifies their binary representations according to specific rules, and prints the modified binary strings along with their lengths. For each input integer, it iterates through its binary representation from least significant bit to most significant bit, applying the following rules: if two consecutive bits are both '1', it changes the first '1' to '-1' and sets a flag; if the flag is set and the current bit is '0', it changes the '0' to '1' and resets the flag; if the flag is set and the current bit is '1', it changes the '1' to '0' and appends an additional '1' to the end of the binary string, increasing its length by 1. After applying these rules, it prints the length of the modified binary string and the string itself. The function repeats this process for each input integer, and upon completion, the standard input is exhausted.

