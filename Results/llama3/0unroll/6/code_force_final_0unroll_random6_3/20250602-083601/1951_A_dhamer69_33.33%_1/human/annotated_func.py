#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (1 <= t <= 1000) and then a binary string of size t.
    t = int(input())
    while t > 0:
        n = int(input())
        
        s = input()
        
        if n == 2:
            if s == '00':
                print('YES')
            else:
                print('NO')
        else:
            count_1 = s.count('1')
            if count_1 % 2 != 0:
                print('NO')
            elif s.count('11') == 1:
                print('NO')
            else:
                print('YES')
        
        t -= 1
        
    #State: The output state is a series of 'YES' or 'NO' strings, each corresponding to whether a given binary string can be rearranged into a sequence of '11's and '00's.

#Overall this is what the function does:Determines whether a given binary string can be rearranged into a sequence of '11's and '00's, and prints 'YES' or 'NO' accordingly for each test case.

