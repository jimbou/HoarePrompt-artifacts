#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 100) and then t integers n (3 <= n <= 78).
    cases = int(input())
    for i in range(cases):
        arr = []
        
        lex = int(input())
        
        for j in range(2):
            if lex <= 26:
                arr.append(1)
                lex = lex - 1
            elif lex < 52:
                arr.append(26)
                lex = lex - 26
            else:
                arr.append(26)
                lex = lex - 26
        
        arr.append(lex)
        
        arr.sort()
        
        for k in range(3):
            print(chr(arr[k] + 96), end='')
        
    #State: cases is 0, i is equal to the initial value of cases, j is 2, k is 3, lex is an integer less than or equal to 25, and arr is a list containing 1, 1, lex if lex was less than or equal to 26, otherwise arr is a list containing 1, 26, 1, lex if lex was greater than 26, and the characters represented by the ASCII values of arr[0] + 96, arr[1] + 96, and arr[2] + 96 are no longer being printed.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each case consists of an integer 't' followed by 't' integers 'n'. For each 'n', it constructs a list of three integers based on the value of 'n', sorts the list, and prints the characters represented by the ASCII values of the sorted list elements plus 96. The function processes all test cases and prints the corresponding characters for each case.

