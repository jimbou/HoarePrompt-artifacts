#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing two integers a and b (1 <= a, b <= 10^9).
    for i in range(int(input())):
        a, b = [int(i) for i in input().split()]
        
        if a % 2 == 0 and b % 2 == 0:
            print('yes')
        elif (a - b == -a, a) or (b - a == -b, b):
            print('no')
        elif (a - b) % 2 > 0 or (a - b) % 2 < 0:
            print('yes')
        else:
            print('no')
        
    #State: `a` and `b` are integers between 1 and 10^9, `i` is t-1, stdin is empty, input() is at least 0. If both `a` and `b` are even numbers, 'yes' is printed. If either `a` or `b` or both are odd, then if `a` is equal to `-b` or `b` is equal to `-a`, 'no' is printed. If the difference between `a` and `b` is odd, 'yes' is printed. Otherwise, 'no' is printed.

#Overall this is what the function does:This function reads a series of pairs of integers from standard input, determines whether the difference between each pair meets certain conditions, and prints 'yes' or 'no' accordingly. The function iterates over the input pairs, checking if both numbers are even, if one is the negative of the other, or if their difference is odd, and prints 'yes' in the first and third cases, and 'no' in the second case. The function continues until all input pairs have been processed, leaving the standard input empty.

