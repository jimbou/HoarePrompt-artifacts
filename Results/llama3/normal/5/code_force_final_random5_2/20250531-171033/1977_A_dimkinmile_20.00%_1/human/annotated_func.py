#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t lines, each containing two integers n and m (1 <= n, m <= 100).
    n, m = map(int, input().split())
    if (n >= m) :
        print('Yes')
        #This is printed: Yes
    else :
        print('No')
        #This is printed: No
    #State: *`n` and `m` are integers between 1 and 100 inclusive, stdin contains an integer t-1 (0 <= t-1 <= 99) followed by t-1 lines, each containing two integers n and m (1 <= n, m <= 100). If `n` is greater than or equal to `m`, 'Yes' is printed. Otherwise, 'No' is printed.

#Overall this is what the function does:This function reads two integers `n` and `m` from standard input and prints 'Yes' if `n` is greater than or equal to `m`, otherwise it prints 'No'. The function modifies the state of the program by consuming two integers from standard input and printing a result, leaving the remaining input unchanged.

