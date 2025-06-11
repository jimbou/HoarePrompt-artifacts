#State of the program right berfore the function call: stdin contains t+1 inputs: first an integer t and then t strings s. t is a positive integer and each s consists only of lowercase Latin letters and/or question marks.
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
        
    #State: The loop will print the length of the longest substring that is a palindrome and has a length of at least 2, and then terminate. The list s and the number n will remain unchanged. The stdin will be empty after reading all t inputs.
    print(0)
    #This is printed: 0

#Overall this is what the function does:This function reads a string from standard input and determines the length of the longest palindromic substring with a length of at least 2. If such a substring is found, it prints the length of the longest palindromic substring and terminates. If no such substring is found, it prints 0. The function does not modify the input string or any other external state.

