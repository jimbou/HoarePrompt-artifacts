#State of the program right berfore the function call: stdin contains two inputs: first an integer (t) and then t integers (n). t is a positive integer and n is an integer such that 2 <= n <= 10^3.
    t = int(input())
    for i in range(t):
        n = int(input())
        
        print('1 1')
        
        print('1 2')
        
        if n == 3:
            print('2 3')
        elif n >= 4:
            print('2 4')
            for j in range(4, n + 1):
                print(str(j) + ' ' + str(j))
        
    #State: `t` is 0, `i` is `t`, `n` is an integer between 2 and 10^3 (inclusive), stdin is empty, '1 1' has been printed `t` times, '1 2' has been printed `t` times. If `n` is 3, '2 3' has been printed `t` times. If `n` is greater than or equal to 4, '2 4' has been printed `t` times, and for all integers `j` from 4 to `n` (inclusive), `j` has been printed followed by a space and `j` has been printed `t` times.

#Overall this is what the function does:This function reads a positive integer t from standard input, followed by t integers n, each between 2 and 10^3 (inclusive). It then prints a series of lines to standard output, where each series consists of '1 1', '1 2', and either '2 3' (if n is 3) or '2 4' followed by 'j j' for all integers j from 4 to n (inclusive). The function repeats this process t times, emptying the standard input in the process.

