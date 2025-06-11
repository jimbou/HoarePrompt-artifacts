#State of the program right berfore the function call: stdin contains t test cases. Each test case contains an integer n followed by n lines each containing a string of n characters '0' or '1'.
    t = int(input())
    for i in range(t):
        n = int(input())
        
        a = 0
        
        b = ''
        
        for j in range(n):
            s = input()
            if s.count('1') == 1:
                a = 'TRIANGLE'
            elif s.count('1') > 1:
                b = 'SQUARE'
        
        if a != 0:
            print(a)
        else:
            print(b)
        
    #State: The output state contains t lines, each containing either 'TRIANGLE' or 'SQUARE'. For each test case, if there is a row with exactly one '1', the output is 'TRIANGLE', otherwise it is 'SQUARE'.

#Overall this is what the function does:Determines and prints the shape of a given grid of '0' and '1' characters for each test case. If a row contains exactly one '1', it outputs 'TRIANGLE'; otherwise, it outputs 'SQUARE'.

