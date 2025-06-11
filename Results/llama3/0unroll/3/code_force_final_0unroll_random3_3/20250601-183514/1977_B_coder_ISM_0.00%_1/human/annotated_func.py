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
        
    #State: The loop will execute t times, each time taking an integer x as input, converting it to binary, and then performing a series of operations on the binary representation. The output will be the length of the modified binary representation and the representation itself. The value of t will remain unchanged.

#Overall this is what the function does:This function reads a number of test cases (t) from standard input, then for each test case, it reads a positive integer (x) and converts it to its binary representation. It then performs a series of operations on the binary representation, including flipping bits and appending new bits, and finally prints the length of the modified binary representation and the representation itself. The function does not return any value, but instead prints the results for each test case.

