#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 50) and then t integers n (2 <= n <= 10^3).
    t = int(input())
    for i in range(t):
        n = int(input())
        
        print('1 1')
        
        print('1 2')
        
        if n == 3:
            print('2 3')
        else:
            print('2 4')
            for j in range(4, n + 1):
                print(str(j) + ' ' + str(j))
        
    #State: `t` is 0, `i` is `t`, `n` is an integer between 2 and 10^3, stdin is empty, and a series of numbers from 1 to `n` are printed, each followed by the same number, and if `n` is not 3, then a series of numbers from 4 to `n` are printed, each followed by the same number.

#Overall this is what the function does:The function reads a series of integers from standard input, where the first integer represents the number of test cases (t), and each subsequent integer (n) represents the number of elements in a sequence. For each sequence, the function prints a series of numbers from 1 to n, each followed by the same number. If n is not 3, it also prints a series of numbers from 4 to n, each followed by the same number. The function consumes all input from standard input and produces the described output.

