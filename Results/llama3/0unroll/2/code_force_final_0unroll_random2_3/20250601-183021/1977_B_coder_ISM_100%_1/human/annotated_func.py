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
        
    #State: The loop has executed t times, and for each execution, it has printed the length of the list s and the elements of the list s. The list s represents a binary number with some modifications. The modifications are as follows: if two consecutive bits are 1, the first bit is changed to -1 and the second bit is changed to 0. If a bit is -1 and the previous bit is 1, the -1 is moved to the previous bit and the current bit is changed to 0. If the last bit is 0 and the flag is 1, the last bit is changed to 1. If the last bit is 1 and the flag is 1, the last bit is changed to 0 and a new bit 1 is appended to the list. The flag is initially 0 and is set to 1 when two consecutive bits are 1. The flag is reset to 0 when a bit is changed from 0 to 1. The loop has finished executing, and the output state is the final state of the variables after all iterations.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case is a single positive integer x. It converts each integer into a binary representation as a list of characters, applies a series of modifications to the binary representation, and then prints the length of the modified binary representation and its elements. The modifications involve changing consecutive '1' bits to '-1' and '0', moving '-1' bits to the previous position if the current bit is '1', and appending or modifying the last bit based on a flag that tracks the presence of consecutive '1' bits. The function repeats this process for each test case and outputs the modified binary representations.

