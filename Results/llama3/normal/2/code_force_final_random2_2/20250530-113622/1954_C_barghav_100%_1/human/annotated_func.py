#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t pairs of integers x and y, where x and y are strings of digits from 1 to 9 and have the same length.
    a = list(input())
    b = list(input())
    f = 0
    for i in range(len(a)):
        if f == 0:
            if a[i] < b[i]:
                a[i], b[i] = b[i], a[i]
                f = 1
            elif a[i] > b[i]:
                f = 1
        elif a[i] > b[i]:
            a[i], b[i] = b[i], a[i]
        
    #State: a is a list of digits from the first pair of integers with all elements being greater than or equal to the corresponding elements of b, b is a list of digits from the second pair of integers, stdin contains t-1 pairs of integers x and y, where x and y are strings of digits from 1 to 9 and have the same length, i is the length of a, f is 1.
    for i in range(len(a)):
        print(a[i], end='')
        
    #State: a is a list of digits from the first pair of integers with all elements being greater than or equal to the corresponding elements of b, b is a list of digits from the second pair of integers, stdin contains t-1 pairs of integers x and y, where x and y are strings of digits from 1 to 9 and have the same length, i is the length of a, f is 1, and all elements of a which are greater than or equal to the corresponding elements of b are printed.
    print()
    #This is printed: nothing
    for i in range(len(b)):
        print(b[i], end='')
        
    #State: `a` is a list of digits from the first pair of integers with all elements being greater than or equal to the corresponding elements of `b`, `b` is a list of digits from the second pair of integers, `stdin` contains `t-1` pairs of integers `x` and `y`, where `x` and `y` are strings of digits from 1 to 9 and have the same length, `i` is equal to the length of `b`, `f` is 1, and all elements of `a` which are greater than or equal to the corresponding elements of `b` are printed, and nothing is printed, and all elements of `b` are printed.
    print()
    #This is printed: Nothing

#Overall this is what the function does:This function takes two pairs of integers as input from the standard input, compares the pairs digit by digit, and prints the pair with the larger or equal digits first, followed by the other pair. If the first pair is smaller, it swaps the pairs before printing. The function repeats this process for multiple pairs of integers, as specified by the initial input.

