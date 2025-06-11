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
        
    #State: Output State: info is a list of lists of integers, where each sublist contains 3 integers, and cases is an integer between 1 and 100, stdin is empty.
    for i in range(cases):
        temp = ''
        
        for j in range(3):
            temp = temp + chr(info[i][j] + 96)
        
        print(temp)
        
    #State: Output State: The output state is a list of lists of integers, where each sublist contains 3 integers, and cases is an integer between 1 and 100, stdin is empty, and the standard output contains a string of lowercase letters, where each letter is the result of adding 96 to the corresponding integer in the info list and converting it to a character using the chr function.

#Overall this is what the function does:This function reads input from standard input, processes it, and prints output to standard output. It accepts an integer t (1 <= t <= 100) followed by t integers n (3 <= n <= 78) as input. The function then converts each integer n into a list of three integers, sorts the list, and appends it to a list of lists. Finally, it prints a string of lowercase letters to standard output, where each letter is the result of adding 96 to the corresponding integer in the list and converting it to a character using the chr function. The function does not return any value.

