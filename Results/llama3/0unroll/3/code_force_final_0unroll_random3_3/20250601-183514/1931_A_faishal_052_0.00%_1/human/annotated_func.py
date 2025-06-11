#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) on the first line, followed by t lines each containing an integer n (3 <= n <= 78).
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
        
    #State: The program will print t lines, each containing three lowercase letters. The letters in each line will be in alphabetical order, and will be determined by the input integer n as follows: if n is between 3 and 26 (inclusive), the letters will be the first n letters of the alphabet; if n is between 27 and 51 (inclusive), the letters will be 'a' followed by the first n-26 letters of the alphabet; if n is between 52 and 78 (inclusive), the letters will be 'a' followed by 'z' followed by the first n-52 letters of the alphabet.

#Overall this is what the function does:The function reads an integer t from standard input, representing the number of test cases. For each test case, it reads an integer n and generates three lowercase letters based on the value of n. If n is between 3 and 26, the letters are the first n letters of the alphabet. If n is between 27 and 51, the letters are 'a' followed by the first n-26 letters of the alphabet. If n is between 52 and 78, the letters are 'a' followed by 'z' followed by the first n-52 letters of the alphabet. The function prints the generated letters in alphabetical order for each test case.

