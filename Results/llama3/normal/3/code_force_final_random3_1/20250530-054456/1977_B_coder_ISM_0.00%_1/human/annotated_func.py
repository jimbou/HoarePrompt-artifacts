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
        
    #State: t is an integer between 1 and 10^4, nalla is t, x is a positive integer less than 2^30, length is 30, stdin contains 0 positive integers x (1 <= x < 2^30), i is 29, The list s contains a string '1' if the bit at position i in the binary representation of x is 1, otherwise it contains '0'. If the bit at position i in the binary representation of x is 1, an additional '1' is appended to the list s. If the bit at position i in the binary representation of x is 0, an extra '0' is appended to the end of the list s. The list s has an additional '1' appended to it if the bit at position i in the binary representation of x is 1, otherwise an extra '0' is appended to the end of the list s, and the list s is printed. If flag is 1 and s[29] is '0', an extra '1' is appended to the end of the list s. Otherwise, the list s is printed as it is. If s[i] is '-1' and s[i - 1] is '1', then the current value of s[i] is '0' and the current value of s[i - 1] is '-1'. s[i] is '0', s[i - 1] is '-1', and the length which is equal to 30 is being printed, and the list s is printed

#Overall this is what the function does:This function reads a series of positive integers from standard input, converts each integer to its binary representation, and then performs a series of operations on the binary representation. For each binary representation, it checks for consecutive '1' bits and replaces them with '-1' and '0' bits, then appends an extra '1' bit if the last bit is '0' and the flag is 1. Finally, it prints the modified binary representation and its length. The function repeats this process for each input integer.

