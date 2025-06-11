#State of the program right berfore the function call: stdin contains t+1 inputs: the first input is an integer t (1 <= t <= 1000), and the rest t inputs are strings consisting only of lowercase Latin letters and/or question marks, each string's length is between 1 and 5000 (inclusive).
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
        
    #State: Output State: The loop will print the length of the longest substring that is the same when reversed, and then exit. The state of the other variables (stdin, s, n) remains unchanged.
    print(0)
    #This is printed: 0

#Overall this is what the function does:This function reads a string from standard input and prints the length of the longest substring that is the same when reversed. If no such substring is found, it prints 0. The function does not modify the input string or any other variables, and it does not return any value.

