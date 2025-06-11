#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by 2t lines, each containing a string of digits from 1 to 9, where the strings on each pair of lines have the same length.
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
        
    #State: `a` is a list of digits from 1 to 9 that is sorted in ascending order, `b` is a list of digits from 1 to 9 that is sorted in descending order, `f` is 1, `stdin` contains t-1 integers followed by 2(t-1) lines, each containing a string of digits from 1 to 9, and `i` is 8.
    for i in range(len(a)):
        print(a[i], end='')
        
    #State: `a` is a list of digits from 1 to 9 that is sorted in ascending order and has 9 elements, `b` is a list of digits from 1 to 9 that is sorted in descending order, `f` is 1, `stdin` contains t-1 integers followed by 2(t-1) lines, each containing a string of digits from 1 to 9, `i` is 8, and the 9th element of the list `a` which is 9 has been printed.
    print()
    #This is printed: a new line
    for i in range(len(b)):
        print(b[i], end='')
        
    #State: `a` is a list of digits from 1 to 9 that is sorted in ascending order and has 9 elements, `b` is a list of digits from 1 to 9 that is sorted in descending order and has 9 elements, `f` is 1, `stdin` contains t-1 integers followed by 2(t-1) lines, each containing a string of digits from 1 to 9, `i` is 8, and the 9th element of the list `a` which is 9 has been printed, and a new line is being printed, and all elements of the list `b` have been printed.
    print()
    #This is printed: a new line

#Overall this is what the function does:This function reads two lines of digits from standard input, sorts the first line in ascending order and the second line in descending order, and then prints the sorted lines. The function repeats this process for a specified number of test cases, where the number of test cases is also read from standard input.

