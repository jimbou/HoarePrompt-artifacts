#State of the program right berfore the function call: stdin contains two inputs: first an integer (1 <= t <= 100) and then t integers (3 <= n <= 78).
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
        
    #State: cases is 0, info is a list containing a sorted list of integers for each of the original t integers in stdin, i is equal to the original value of cases, j is 0, arr is an empty list, lex is an integer between -130 and 25 if the original value of lex was less than 28, or an integer between 2 and 25 if the original value of lex was greater than or equal to 28 and less than 52, or an integer between 26 and 52 if the original value of lex was greater than or equal to 52 and less than or equal to 78, stdin contains no input.
    for i in range(cases):
        temp = ''
        
        for j in range(3):
            temp = temp + chr(info[i][j] + 96)
        
        print(temp)
        
    #State: `cases` is 0, `i` is equal to the original value of cases, `info` is a list containing a sorted list of integers for each of the original t integers, `j` is 3, `arr` is an empty list, `lex` is an integer between -130 and 25 if the original value of lex was less than 28, or an integer between 2 and 25 if the original value of lex was greater than or equal to 28 and less than 52, or an integer between 26 and 52 if the original value of lex was greater than or equal to 52 and less than or equal to 78, `temp` is a string containing three characters with ASCII values equal to `info[i-1][0] + 96`, `info[i-1][1] + 96`, and `info[i-1][2] + 96` respectively, stdin contains no input, and nothing is being printed, and this is printed: a string containing three characters with ASCII values equal to `info[i-1][0] + 96`, `info[i-1][1] + 96`, and `info[i-1][2] + 96` respectively.

#Overall this is what the function does:This function reads a series of integers from standard input, converts each integer into a three-character string using a specific encoding scheme, and prints the resulting strings. The function takes no parameters and returns no value, but instead prints the encoded strings to the console. The encoding scheme involves subtracting 96 from each integer to obtain an ASCII value, and then converting the ASCII value to a character. The function processes each integer in the input sequence independently, and the output strings are printed in the order they are processed.

