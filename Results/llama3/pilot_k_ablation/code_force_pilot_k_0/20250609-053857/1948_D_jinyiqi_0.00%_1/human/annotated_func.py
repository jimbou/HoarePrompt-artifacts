#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t strings, each consisting only of lowercase Latin letters and/or question marks, and the length of each string is between 1 and 5000 (inclusive).
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
        
    #State: The output state will be the length of the longest substring with the same characters or '?' repeated twice, or 0 if no such substring is found. The input string s and the value of n remain unchanged.
    return 0
    #The program returns 0, which represents that no substring with the same characters or '?' repeated twice is found in the input string s.

#Overall this is what the function does:This function determines the length of the longest substring with the same characters or '?' repeated twice in a given input string. It iterates through the string, comparing characters and counting consecutive matches or '?' characters. If a match of the desired length is found, it prints the length of the match multiplied by 2 and returns. If no such match is found after iterating through the entire string, it returns 0, indicating that no substring with the same characters or '?' repeated twice exists in the input string. The input string and its length remain unchanged throughout the process.

