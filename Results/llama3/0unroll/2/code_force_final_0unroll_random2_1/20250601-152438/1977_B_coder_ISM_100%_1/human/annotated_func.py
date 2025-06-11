#State of the program right berfore the function call: stdin contains multiple test cases. The first line of input contains a single integer t (1 <= t <= 10^4) — the number of test cases. Each test case contains a single positive integer x (1 <= x < 2^30).
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
        
    #State: Output State: The output state will be the number of test cases (t) followed by the modified binary representation of each test case. The binary representation will have the following properties: 
    #- If two consecutive bits are '1', the first bit will be changed to '-1' and the second bit will be changed to '0'.
    #- If a '1' is followed by a '0', the '0' will be changed to '1'.
    #- If a '1' is followed by another '1' and a '0', the first '1' will be changed to '-1', the second '1' will be changed to '0', and the '0' will be changed to '1'.
    #- If the last bit is '0' and the flag is set, the last bit will be changed to '1'.
    #- If the last bit is '1' and the flag is set, the last bit will be changed to '0' and an additional '1' will be appended to the end.
    #- If a '-1' is followed by a '1', the '-1' will be moved to the left and the '1' will be changed to '0'.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case is a positive integer. It then modifies the binary representation of each integer according to specific rules, including replacing consecutive '1's, changing '1' followed by '0' to '0' followed by '1', and adjusting the last bit based on a flag. The function outputs the length of the modified binary representation and the representation itself, with any necessary adjustments to handle '-1' and '1' combinations.

