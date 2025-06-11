#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing three integers k, x, and a (2 <= k <= 30, 1 <= x <= 100, 1 <= a <= 10^9).
    for s in [*open(0)][1:]:
        k, x, a = map(int, s.split())
        
        if x < k - 1:
            if a >= x + 1:
                print('YES')
            else:
                print('NO')
        elif x == k - 1:
            if a >= x + 2:
                print('YES')
            else:
                print('NO')
        else:
            z = k - 2
            for i in range(x - k + 3):
                z += z // (k - 1) + 1
            if a >= z:
                print('YES')
            else:
                print('NO')
        
    #State: `k`, `x`, `a` are integers, and stdin contains at least one line. If `x` is less than `k-1`, then if `a` is greater than or equal to `x` plus 1, 'YES' is printed. Otherwise, 'NO' is printed. If `x` is equal to `k-1`, then if `a` is greater than or equal to `x` plus 2, 'YES' is printed. Otherwise, 'NO' is printed. If `x` is greater than `k-1`, then `z` is calculated by repeating the expression `k-2 + (k-2) // (k - 1) + 1` `x - k + 3` times, and if `a` is greater than or equal to `z`, 'YES' is printed. Otherwise, 'NO' is printed.

#Overall this is what the function does:Determines whether a given number 'a' is sufficient to cover a sequence of operations based on the values of 'k' and 'x', and prints 'YES' if sufficient, 'NO' otherwise. The function processes multiple test cases from standard input, where each case consists of three integers 'k', 'x', and 'a'.

