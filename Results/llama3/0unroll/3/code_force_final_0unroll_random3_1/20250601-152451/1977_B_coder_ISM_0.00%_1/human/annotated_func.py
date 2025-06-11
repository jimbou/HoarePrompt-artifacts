#State of the program right berfore the function call: stdin contains multiple test cases. The first line of input contains a single integer t (1 <= t <= 10^4) — the number of test cases. The description of the test cases follows. Each test case contains a single positive integer x (1 <= x < 2^30).
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
        
    #State: The loop will execute 't' number of times, where 't' is the number of test cases. For each test case, it will read a positive integer 'x' from the standard input. It will then convert the binary representation of 'x' into a list of characters 's', where '1' represents a set bit and '0' represents an unset bit. It will then perform a series of operations on 's' to transform it into a new binary representation. The transformed binary representation will be printed to the standard output, along with its length. The output will be in the format of a list of characters, where '1' represents a set bit, '0' represents an unset bit, and '-1' represents a bit that has been flipped. The length of the transformed binary representation will also be printed.

#Overall this is what the function does:This function reads a number of test cases from standard input, then for each test case, it reads a positive integer, converts it to its binary representation, performs a series of bit manipulation operations on it, and prints the transformed binary representation along with its length. The bit manipulation operations involve flipping bits, setting bits, and potentially appending an additional bit to the end of the representation. The function executes this process for each test case, producing a transformed binary representation for each input integer.

