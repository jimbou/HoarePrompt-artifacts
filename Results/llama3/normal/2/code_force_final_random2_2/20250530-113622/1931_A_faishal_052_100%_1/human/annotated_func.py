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
        
    #State: cases is 0, info is a list containing t sorted lists of integers, each containing either the integer 1, the integer 26, or both, and an integer between -25 and 77 inclusive, i is t-1, j is 0, stdin is empty, and arr is a sorted list containing either the integer 1, the integer 26, or both, and an integer between -25 and 77 inclusive.
    for i in range(cases):
        temp = ''
        
        for j in range(3):
            temp = temp + chr(info[i][j] + 96)
        
        print(temp)
        
    #State: cases is equal to t, i is equal to t-1, j is 3, temp is a string containing three characters, where the first character is the character corresponding to the ASCII value of info[t-1][0] + 96, the second character is the character corresponding to the ASCII value of info[t-1][1] + 96, and the third character is the character corresponding to the ASCII value of info[t-1][2] + 96, and this string temp is being printed, and info is a list containing t sorted lists of integers, each containing either the integer 1, the integer 26, or both, and an integer between -25 and 77 inclusive, and arr is a sorted list containing either the integer 1, the integer 26, or both, and an integer between -25 and 77 inclusive.

#Overall this is what the function does:This function reads a series of integers from standard input, processes them into a specific format, and prints out a string of three characters for each integer. The function takes no parameters and returns no value. It reads an integer t, followed by t integers n, where each n is processed into a list of three integers. The function then converts each list of integers into a string of three characters, where each character corresponds to the ASCII value of the integer plus 96. The function prints out each string of three characters. The final state of the program is that the input has been processed and the resulting strings have been printed to the console.

