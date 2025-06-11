#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by 2t lines, each containing a string of digits from 1 to 9. The strings on each pair of lines have the same length.
    a = list(input())
    b = list(input())
    for i in range(len(a)):
        if i <= len(a) // 2 - 1:
            n = min(a[i], b[i])
            m = max(a[i], b[i])
            a[i] = m
            b[i] = n
        else:
            n = min(a[i], b[i])
            m = max(a[i], b[i])
            a[i] = n
            b[i] = m
        
    #State: a is a list of digits from the first string of digits from stdin, b is a list of digits from the second string of digits from stdin, stdin contains t-1 pairs of strings of digits, each pair having the same length. The digits in a and b are sorted in ascending order.
    for i in range(len(a)):
        print(a[i], end='')
        
    #State: `a` is a list of digits from the first string of digits from stdin that is not empty, `b` is a list of digits from the second string of digits from stdin, stdin contains t-1 pairs of strings of digits, each pair having the same length. The digits in `a` and `b` are sorted in ascending order, `i` is equal to the length of `a`, and all elements of the list `a` have been printed in ascending order.
    print()
    #This is printed: a newline
    for i in range(len(b)):
        print(b[i], end='')
        
    #State: `a` is a list of digits from the first string of digits from stdin that is not empty, `b` is a list of digits from the second string of digits from stdin that must have at least 3 elements, stdin contains t-1 pairs of strings of digits, each pair having the same length. The digits in `a` and `b` are sorted in ascending order, `i` is equal to the length of `b`, and all elements of the list `b` have been printed in ascending order, and a new line is printed
    print()
    #This is printed: a new line

#Overall this is what the function does:This function reads two strings of digits from standard input, sorts the first half of the digits in ascending order and the second half in descending order, and then prints the sorted digits in ascending order, followed by a newline. The function repeats this process for multiple pairs of strings, where the number of pairs is specified by an integer at the beginning of the input.

