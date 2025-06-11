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
        
    #State: cases is 0, i is equal to the initial value of cases, j is 2, k is 3, lex is an integer, arr is a sorted list containing either 1 or 26, and the characters represented by the ASCII values of 96 + 1, 96 + 26, and 96 + lex are being printed. If lex is less than or equal to 25, lex is an integer with a value less than or equal to 25 and arr contains 1. If lex is larger than 25 and less than 52, lex is an integer larger than 25 and less than 52 and arr contains 26.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each case consists of an integer. For each case, it generates a sorted list of three integers, either 1 or 26, and a remaining value, then prints the corresponding lowercase letters represented by the ASCII values of 96 plus these integers. The function processes all test cases and prints the resulting characters for each case.

