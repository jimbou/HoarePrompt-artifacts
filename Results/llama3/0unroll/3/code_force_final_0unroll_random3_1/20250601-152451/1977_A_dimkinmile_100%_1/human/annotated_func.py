#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains one integer t (1 ≤ t ≤ 100). Each of the following t lines contains two integers n and m (1 ≤ n, m ≤ 100).
    n, m = map(int, input().split())
    if ((n - m) % 2 == 0 and n - m >= 0) :
        print('Yes')
        #This is printed: Yes
    else :
        print('No')
        #This is printed: No
    #State: *`n` and `m` are integers between 1 and 100, stdin contains multiple lines of input. The first line contains one integer t-1 (0 ≤ t-1 ≤ 99). Each of the following t-1 lines contains two integers n and m (1 ≤ n, m ≤ 100). If the difference between `n` and `m` is even and non-negative, 'Yes' is printed. Otherwise, 'No' is printed.

#Overall this is what the function does:This function reads two integers `n` and `m` from standard input and prints 'Yes' if the difference between `n` and `m` is even and non-negative, otherwise it prints 'No'. The function does not modify the input values or the state of the program, it only prints a message based on the condition.

