#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 100). Each of the following t lines contains two integers n and m (1 <= n, m <= 100).
    n, m = map(int, input().split())
    if (n >= m) :
        print('Yes')
        #This is printed: Yes
    else :
        print('No')
        #This is printed: No
    #State: `n` and `m` are integers between 1 and 100, and stdin contains t-1 lines of input where t is an integer between 1 and 100. If `n` is greater than or equal to `m`, 'Yes' is printed. Otherwise, 'No' is printed.

#Overall this is what the function does:This function compares two integers, `n` and `m`, and prints 'Yes' if `n` is greater than or equal to `m`, and 'No' otherwise. It consumes a line of input from stdin containing the two integers, leaving `t-1` lines of input remaining, where `t` is an integer between 1 and 100.

