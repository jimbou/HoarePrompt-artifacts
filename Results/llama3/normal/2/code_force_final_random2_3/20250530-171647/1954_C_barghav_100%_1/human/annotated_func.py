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
        
    #State: `a` is a list of digits from the first pair of integers, `b` is a list of digits from the second pair of integers, `f` is 1, `stdin` contains t-1 pairs of integers x and y, where x and y are strings of digits from 1 to 9 and have the same length, `i` is equal to the length of `a`.
    for i in range(len(a)):
        print(a[i], end='')
        
    #State: `a` is a list of digits from the first pair of integers that must have at least `i` elements, `b` is a list of digits from the second pair of integers, `f` is 1, `stdin` contains t-1 pairs of integers x and y, where x and y are strings of digits from 1 to 9 and have the same length, `i` is equal to the length of `a`, and all elements of the list `a` have been printed
    print()
    #This is printed: a newline (empty line)
    for i in range(len(b)):
        print(b[i], end='')
        
    #State: `a` is a list of digits from the first pair of integers that must have at least `i` elements, `b` is a list of digits from the second pair of integers that must have at least `i` elements, `f` is 1, `stdin` contains t-1 pairs of integers x and y, where x and y are strings of digits from 1 to 9 and have the same length, `i` is equal to the length of `b`, all elements of the list `a` have been printed, and a new line is printed, and all elements of the list `b` have been printed.
    print()
    #This is printed: a new line

#Overall this is what the function does:This function takes two pairs of integers as input from the standard input, compares them digit by digit, and prints the digits of the larger number first, followed by the digits of the smaller number. If the numbers are equal, it prints the digits of the first number first. The function then prints a newline character after printing each number. The function repeats this process for all pairs of integers in the input, which is specified by an integer t at the beginning of the input.

