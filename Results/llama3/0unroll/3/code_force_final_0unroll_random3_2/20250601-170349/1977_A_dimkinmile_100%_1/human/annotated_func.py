#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t lines, each containing two integers n and m (1 <= n, m <= 100).
    n, m = map(int, input().split())
    if ((n - m) % 2 == 0 and n - m >= 0) :
        print('Yes')
        #This is printed: Yes
    else :
        print('No')
        #This is printed: No
    #State: *`n` and `m` are integers, 1 <= n, m <= 100, stdin contains an integer t-1 (0 <= t-1 <= 99) followed by t-1 lines, each containing two integers n and m (1 <= n, m <= 100). If the difference between `n` and `m` is even and greater than or equal to 0, 'Yes' is printed. Otherwise, 'No' is printed.

#Overall this is what the function does:This function reads two integers `n` and `m` from standard input, checks if their difference is even and non-negative, and prints 'Yes' if the condition is met, otherwise prints 'No'. The function modifies the state of the standard input by consuming the two integers, leaving the remaining input unchanged.

