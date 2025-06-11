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
        
    #State: t is 0, nalla is t, length is either 30 or 31, stdin contains no test cases, i is equal to length, x is an integer, s is a list containing either 30 or 31 strings where each element at index j is '1' if the bit at position j in the binary representation of x is 1, '0' otherwise, except for the last element which is either '-1', '0' or '1' respectively. If flag is 1 and the last element of s is '0', then flag is 1 and the last element of s is '1'. If flag is 1 and the last element of s is not '0', then length is 31 and the last two elements of s are '0' and '1' respectively. Otherwise, length is 30 and the last element of s is '-1'. For all indices i where the condition (s[i] == '-1') & (s[i - 1] == '1') is true, s[i] is '0' and s[i - 1] is '-1', and the list s and the length which is either 30 or 31 are being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case is a single positive integer x. For each test case, it converts the integer to its binary representation, modifies the binary string by applying a set of rules, and then prints the length of the modified binary string and the string itself. The rules involve flipping bits, inserting a new bit, and swapping bits under certain conditions. The function processes all test cases and prints the modified binary strings and their lengths.

