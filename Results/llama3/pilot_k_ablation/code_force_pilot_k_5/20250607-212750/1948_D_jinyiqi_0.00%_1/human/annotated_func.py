#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t strings, each consisting of lowercase Latin letters and/or question marks, with a length between 1 and 5000.
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
        
    #State: The loop will terminate after printing the maximum possible value of `count * 2` for each string in `stdin`, or without printing anything if no such value is found.
    return 0
    #The program returns 0

#Overall this is what the function does:This function reads strings from standard input, determines the maximum possible value of consecutive matching characters (ignoring question marks) in each string, and prints this value multiplied by 2. If no such value is found, it prints nothing. The function returns 0 in all cases.

