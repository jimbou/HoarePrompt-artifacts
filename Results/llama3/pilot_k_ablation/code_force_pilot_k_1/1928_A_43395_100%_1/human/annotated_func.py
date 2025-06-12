#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing two integers a and b (1 <= a, b <= 10^9).
    for i in range(int(input())):
        a, b = [int(i) for i in input().split()]
        
        if a % 2 == 0 and b % 2 == 0:
            print('yes')
        elif a % 2 == 0 and a / 2 != b or b % 2 == 0 and b / 2 != a:
            print('yes')
        else:
            print('no')
        
    #State: stdin is empty, `i` is equal to the initial value of `t`, for each pair of integers `a` and `b` that were in stdin, either 'yes' or 'no' has been printed to the console, indicating whether `a` is equal to `b / 2` or `b` is equal to `a / 2` when either `a` or `b` is even, or whether both `a` and `b` are even.

#Overall this is what the function does:This function reads a series of pairs of integers from standard input, determines whether each pair meets certain conditions (either both numbers are even, or one number is half the other when one of them is even), and prints 'yes' or 'no' to the console for each pair, indicating whether the condition is met. The function continues this process until all input pairs have been processed, at which point the standard input is empty.

