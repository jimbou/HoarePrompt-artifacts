#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 1000) and then t strings, each consisting of 1 to 5000 lowercase Latin letters and/or question marks.
    for j in range(n // 2, 0, -1):
        count = 0
        
        for k in range(0, n - j):
            if s[k] == '?' or s[k + j] == '?' or s[k] == s[k + j]:
                count += 1
            else:
                count = 0
            if count == j:
                print(count * 2)
                return
        
    #State: `n` is at least 1, `j` is 0, `count` is 0, stdin contains two inputs: first an integer `t` (1 <= `t` <= 1000) and then `t` strings, each consisting of 1 to 5000 lowercase Latin letters and/or question marks. If a sequence of `j` consecutive pairs of characters in `s` are either equal or contain a '?', then the loop has printed `j * 2` and terminated. Otherwise, the loop has completed all iterations without printing anything.
    return 0
    #The program returns 0.

#Overall this is what the function does:This function takes a string `s` of lowercase Latin letters and/or question marks as input and checks for sequences of consecutive pairs of characters that are either equal or contain a '?'. If such a sequence is found, the function prints the length of the sequence multiplied by 2 and terminates. If no such sequence is found after checking all possible sequences, the function returns 0.

