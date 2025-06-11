#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t strings, each consisting only of lowercase Latin letters and/or question marks, and the length of each string is between 1 and 5000 (inclusive).
    s = list(input())
    n = len(s)
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
        
    #State: `count` is 0 or a multiple of `j`, `stdin` contains `t-1` strings, each consisting only of lowercase Latin letters and/or question marks, and the length of each string is between 1 and 5000 (inclusive), `s` is a list of characters from the first string, `n` is at least 2, `j` is 1, `k` is `n - 1`.
    print(0)
    #This is printed: 0

#Overall this is what the function does:This function reads a string from standard input and checks for repeated patterns within the string. It prints the length of the longest repeated pattern found, or 0 if no pattern is found. The function processes one string at a time, and after processing, the standard input is left with the remaining strings.

