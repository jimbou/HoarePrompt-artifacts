#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains one input: an integer n (1 <= n <= 500).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        sum = 1
        
        for i in range(2, n + 1):
            sum += (i * i - (i - 1) * (i - 1)) * i
        
        print(sum, n + n)
        
        for j in range(1, n + 1):
            print(1, n - j + 1, *range(1, n + 1))
            print(2, n - j + 1, *range(1, n + 1))
        
    #State: `t` is an integer equal to 0, `n` is an integer that must be at least `n`, `sum` is 1 + ∑((i * i - (i - 1) * (i - 1)) * i) for `i` from 2 to `n`, `_` is `t`, `stdin` contains multiple test cases minus `t` test cases, `i` is `n + 1`, `j` is `n + 1`, and the sum which is equal to 1 + ∑((i * i - (i - 1) * (i - 1)) * i) for `i` from 2 to `n` and the value of `n` plus `n` which is equal to 2 * `n` are printed, and this is printed: 1, `n-j+1`, and the numbers from 1 to `n` inclusive, which are the numbers from 1 to `n`, and this is printed: 2, `n-j+1`, and the numbers from 1 to `n` inclusive, which are the numbers from 1 to `n`, for each iteration of the loop.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains a single integer n. For each test case, it calculates a sum using a formula and prints the sum along with the value of n plus n. Additionally, it prints a series of numbers in a specific pattern for each iteration of a loop. The function does not return any value but modifies the standard output by printing the calculated sum and the series of numbers.

