#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 1000) and then t strings, each consisting only of lowercase Latin letters and/or question marks.
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
        
    #State: count is 0, stdin contains 1 input: an integer t (1 <= t <= 1000), s is a list of characters from the first input string, n is the length of the first input string and must be at least 2, j is 0, k is n.
    print(0)
    #This is printed: 0

#Overall this is what the function does:This function determines the length of the longest substring in a given string that is a palindrome, where '?' is considered a wildcard character that can match any character. It takes a string as input, checks for palindromic substrings of decreasing lengths, and returns the length of the longest palindromic substring found. If no palindromic substring is found, it returns 0.

