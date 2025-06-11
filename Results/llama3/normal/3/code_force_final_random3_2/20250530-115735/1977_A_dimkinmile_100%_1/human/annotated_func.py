#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t lines, each containing two integers n and m (1 <= n, m <= 100).
    n, m = map(int, input().split())
    if ((n - m) % 2 == 0 and n - m >= 0) :
        print('Yes')
        #This is printed: Yes
    else :
        print('No')
        #This is printed: No
    #State: *`n` and `m` are integers between 1 and 100, stdin contains t-1 lines, each containing two integers n and m (1 <= n, m <= 100), where t is an integer between 1 and 100. If the difference between `n` and `m` is even and non-negative, 'Yes' is printed. Otherwise, if the difference between `n` and `m` is odd or negative, 'No' is printed.

#Overall this is what the function does:Determines whether the difference between two input integers is even and non-negative, and prints 'Yes' if true, otherwise prints 'No'.

