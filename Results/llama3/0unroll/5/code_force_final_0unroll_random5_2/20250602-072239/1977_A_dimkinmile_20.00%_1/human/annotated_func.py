#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 100). Each of the following t lines contains two integers n and m (1 <= n, m <= 100).
    n, m = map(int, input().split())
    if (n >= m) :
        print('Yes')
        #This is printed: Yes
    else :
        print('No')
        #This is printed: No
    #State: *`n` and `m` are integers between 1 and 100, stdin contains multiple lines of input, the first line contains a single integer t-1 (0 <= t-1 <= 99), each of the following t-1 lines contains two integers n and m (1 <= n, m <= 100). If `n` is greater than or equal to `m`, 'Yes' is being printed. Otherwise, 'No' is being printed.

#Overall this is what the function does:This function reads two integers `n` and `m` from the standard input, compares their values, and prints 'Yes' if `n` is greater than or equal to `m`, and 'No' otherwise. The function does not modify the input values or the state of the standard input, but it consumes one line of input. The function's purpose is to determine and print whether the first integer is greater than or equal to the second integer.

