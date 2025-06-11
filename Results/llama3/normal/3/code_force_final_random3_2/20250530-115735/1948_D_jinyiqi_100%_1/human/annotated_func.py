#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t strings, each consisting of lowercase Latin letters and/or question marks, with a length between 1 and 5000.
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
        
    #State: count is 0 or a multiple of j, stdin contains t-1 strings, each consisting of lowercase Latin letters and/or question marks, with a length between 1 and 5000, s is a list of characters from the first string, n is at least 2, j is 1, k is n - 1. If the loop finishes without printing, then count is 0. Otherwise, count is a multiple of j and the loop prints count * 2.
    print(0)
    #This is printed: 0

#Overall this is what the function does:This function reads a string from standard input, checks for matching characters at certain distances, and prints the length of the longest sequence of matching characters found. If no matching sequence is found, it prints 0. The function processes one string at a time, and the input is expected to contain multiple strings separated by newline characters.

