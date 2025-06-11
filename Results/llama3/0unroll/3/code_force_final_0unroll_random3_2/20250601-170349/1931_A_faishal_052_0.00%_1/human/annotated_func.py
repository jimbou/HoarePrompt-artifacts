#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases), then a series of integers (the encoded words), each on a new line. The number of test cases is between 1 and 100, and each encoded word is between 3 and 78.
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
        
    #State: The output state will be a series of strings, each consisting of three lowercase letters, printed to the console. The letters are determined by the encoded words in the input, which are decoded using a specific algorithm. The decoded letters are then sorted in ascending order and printed to the console. The number of strings printed is equal to the value of the `cases` variable.

#Overall this is what the function does:This function reads a series of encoded words from standard input, decodes each word into three lowercase letters using a specific algorithm, sorts the letters in ascending order, and prints them to the console. The function processes a specified number of test cases, where each test case corresponds to a single encoded word. The output is a series of strings, each consisting of three lowercase letters, with the number of strings equal to the number of test cases.

