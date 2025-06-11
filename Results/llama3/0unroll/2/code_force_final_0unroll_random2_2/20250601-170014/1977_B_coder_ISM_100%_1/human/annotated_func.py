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
        
    #State: The loop will print the length and binary representation of each input number x after applying a series of operations to the binary representation. The operations involve flipping bits, inserting a new bit, and shifting bits. The output will be a sequence of binary digits (0s and 1s) with a possible additional bit appended at the end. The length of the output will be between 30 and 31.

#Overall this is what the function does:The function reads a series of positive integers from standard input, applies a series of bit manipulation operations to each integer's binary representation, and prints the resulting binary representation along with its length. The operations involve flipping bits, inserting a new bit, and shifting bits, resulting in a binary sequence of length 30 or 31.

