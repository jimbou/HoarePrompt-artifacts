#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 50) and then t integers n (2 <= n <= 10^3).
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
        
    #State: `t` is an integer between 1 and 50 (inclusive), `i` is `t`, `n` is an integer that was previously in stdin, stdin contains no input, '1 1' is printed, '1 2' is printed. If `n` is 3, '2 3' is printed. If `n` is greater than or equal to 4, `j` is `n`, and all numbers from 4 to `n` (inclusive) are printed with themselves, and '1 1' is printed, '1 2' is printed. Additionally, if `n` is not 3, the same output as the previous case is produced.

#Overall this is what the function does:The function reads a series of integers from standard input, where the first integer represents the number of test cases (t) and each subsequent integer represents a value (n) for each test case. For each test case, the function prints a series of numbers in a specific pattern: it always prints '1 1' and '1 2', and then either '2 3' if n is 3, or all numbers from 4 to n (inclusive) paired with themselves if n is 4 or greater. The function repeats this process for each test case and does not return any value.

