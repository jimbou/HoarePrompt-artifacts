#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then a list of integers (the encoded words). The number of test cases is a positive integer less than or equal to 100. The encoded words are integers between 3 and 78 (inclusive).
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
        
    #State: cases is a positive integer less than or equal to 100, info is a list of lists of integers, stdin contains no input: all inputs have been read by the loop.
    for i in range(cases):
        temp = ''
        
        for j in range(3):
            temp = temp + chr(info[i][j] + 96)
        
        print(temp)
        
    #State: Output State: The loop has printed 'cases' number of strings to the console, each string consisting of three lowercase letters. The letters in each string are determined by the corresponding sublist in the 'info' list. The value of 'cases' and 'info' remain unchanged.

#Overall this is what the function does:Reads a specified number of encoded words from standard input, decodes each word into a three-letter string, and prints the decoded strings to the console. The function does not return any value, and the input variables remain unchanged after execution.

