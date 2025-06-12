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
        
    #State: `t` is 0, `i` is between 1 and 50 (inclusive), `n` is not defined, stdin contains no inputs, '1 1' and '1 2' have been printed t times. If any `n` is 3, '2 3' has been printed, if any `n` is greater than or equal to 4, '2 4' has been printed, and all numbers from 4 to `n` have been printed with themselves as "number number" for each such `n`.

#Overall this is what the function does:This function reads a series of integers from standard input, where the first integer t represents the number of test cases, and each subsequent integer n represents the size of a sequence. For each test case, the function prints a sequence of pairs of numbers, starting with '1 1' and '1 2', and then either '2 3' if n is 3, or '2 4' followed by pairs of numbers from 4 to n (inclusive) if n is 4 or greater. The function repeats this process t times, consuming all input from standard input and producing a series of printed pairs of numbers.

