#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t integers n (3 <= n <= 78).
    cases = int(input())
    info = []
    for i in range(cases):
        arr = []
        
        lex = int(input())
        
        for j in range(2):
            if lex < 28:
                arr.append(1)
                lex = lex - 1
            elif lex < 52:
                arr.append(26)
                lex = lex - 26
            elif lex <= 78:
                arr.append(26)
                lex = lex - 26
        
        arr.append(lex)
        
        arr.sort()
        
        info.append(arr)
        
    #State: cases is 0, info is a list containing cases number of sorted lists of integers that include lex and 1, 1, and 1 or 1, 1, and 26 or 1, 26, and 26, stdin contains 0 integers n (3 <= n <= 78), i is cases, j is 0, 2 is greater than 0.
    for i in range(cases):
        temp = ''
        
        for j in range(3):
            temp = temp + chr(info[i][j] + 96)
        
        print(temp)
        
    #State: `cases` is at least `cases`, `i` is equal to `cases`, `info` is a list containing `cases` number of sorted lists of integers that include lex and 1, 1, and 1 or 1, 1, and 26 or 1, 26, and 26, `stdin` contains `cases` integers `n` (3 <= `n` <= 78), `j` is 3, `temp` is a string containing three characters which are the lowercase letters corresponding to the values of `info[cases-1][0]`, `info[cases-1][1]`, and `info[cases-1][2]`, and this is printed: a string of three lowercase letters corresponding to the values of `info[cases-1][0]`, `info[cases-1][1]`, and `info[cases-1][2]`.

#Overall this is what the function does:This function reads a series of integers from standard input, converts each integer into a corresponding sequence of three lowercase letters based on a specific encoding scheme, and prints these sequences. The encoding scheme involves subtracting 1 or 26 from the input integer to determine the corresponding letters. The function processes multiple test cases, where each test case consists of an integer followed by that many input integers. The function prints the encoded sequences for all test cases.

