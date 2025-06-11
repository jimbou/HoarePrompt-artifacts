#State of the program right berfore the function call: stdin contains two inputs: first an integer (1 <= t <= 1000) and then t strings. Each string consists only of lowercase Latin letters and/or question marks and its length is between 1 and 5000 (inclusive).
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
        
    #State: The loop will print the length of the longest substring that is a palindrome and has at least one '?' character, and then terminate. The value of t, s, and n will remain unchanged.
    print(0)
    #This is printed: 0

#Overall this is what the function does:This function reads a string from standard input and finds the length of the longest substring that is a palindrome and has at least one '?' character. If such a substring exists, it prints its length and terminates; otherwise, it prints 0. The function does not modify the input string or any other external state.

