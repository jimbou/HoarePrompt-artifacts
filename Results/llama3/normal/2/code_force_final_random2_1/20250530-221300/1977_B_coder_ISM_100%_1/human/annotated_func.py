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
        
    #State: t is a positive integer greater than or equal to 0, nalla is equal to t, x is an integer, length is either 30 or 31, stdin contains 0 inputs, s is a list of either 30 or 31 elements where each element is either '1' if the bit at the corresponding position of x is 1 or '0' if the bit at the corresponding position of x is 0. If the element at index i of s is '-1' and the element at index i-1 of s is '1', then the element at index i of s is '0' and the element at index i-1 of s is '-1'. Otherwise, the state of s remains unchanged. i is equal to length-1, and the list s which is either 30 or 31 elements where each element is either '1' if the bit at the corresponding position of x is 1 or '0' if the bit at the corresponding position of x is 0. If the element at index i of s is '-1' and the element at index i-1 of s is '1', then the element at index i of s is '0' and the element at index i-1 of s is '-1'. Otherwise, the state of s remains unchanged is being printed

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case is a single positive integer x. It then converts each integer into a binary string, applies a series of bit manipulation rules to the string, and prints the resulting string along with its length. The rules involve flipping bits, inserting new bits, and swapping bits based on certain conditions. The function processes all test cases and prints the modified binary strings and their lengths.

