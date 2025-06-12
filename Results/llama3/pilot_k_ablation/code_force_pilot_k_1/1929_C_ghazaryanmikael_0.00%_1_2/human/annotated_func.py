#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains one integer t (1 <= t <= 1000). Each of the following t lines contains three integers k, x, and a (2 <= k <= 30, 1 <= x <= 100, 1 <= a <= 10^9).
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 0
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('YES' if a >= s else 'NO')
        
    #State: `stdin` is empty, `k`, `x`, and `a` are the values from the last line of input, `s` is the sum of `x` times (`s // (k - 1) + 1`) for the last line of input, and either 'YES' or 'NO' is printed for each line of input depending on whether `a` is greater than or equal to `s` or not.

#Overall this is what the function does:This function reads multiple lines of input from stdin, where the first line contains an integer t, and each of the following t lines contains three integers k, x, and a. For each line of input, it calculates a sum s by iteratively adding (s // (k - 1) + 1) x times, and then prints 'YES' if a is greater than or equal to s, and 'NO' otherwise. After processing all lines of input, stdin is empty, and the last values of k, x, a, and s are retained.

