#State of the program right berfore the function call: stdin contains two inputs: first an integer (1 ≤ t ≤ 100) and then t integers (3 ≤ n ≤ 78).
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
        
    #State: Output State: info is a list of lists, where each sublist contains three integers representing the number of 1s, 26s, and the remaining value, respectively, for each test case.
    for i in range(cases):
        temp = ''
        
        for j in range(3):
            temp = temp + chr(info[i][j] + 96)
        
        print(temp)
        
    #State: Output State: The output state is a list of strings, where each string contains three characters representing the number of 1s, 26s, and the remaining value, respectively, for each test case. The characters are represented as lowercase letters, where 'a' represents 1, 'z' represents 26, and so on.

#Overall this is what the function does:The function reads input from stdin, processes it, and prints output to stdout. It accepts two types of inputs: an integer (1 ≤ t ≤ 100) and t integers (3 ≤ n ≤ 78). The function then converts each integer into a list of three integers representing the number of 1s, 26s, and the remaining value, respectively. Finally, it prints a list of strings, where each string contains three characters representing the number of 1s, 26s, and the remaining value, respectively, for each test case. The characters are represented as lowercase letters, where 'a' represents 1, 'z' represents 26, and so on.

