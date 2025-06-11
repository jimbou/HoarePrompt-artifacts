#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t pairs of integers x and y, where x and y are strings of digits from 1 to 9 and have the same length.
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
        
    #State: `a` and `b` are lists of digits where the first half of the elements are the maximum and minimum of the original elements of `a` and `b` respectively, and the second half of the elements are the minimum and maximum of the original elements of `a` and `b` respectively. `i` is equal to the length of `a`.
    for i in range(len(a)):
        print(a[i], end='')
        
    #State: `a` is a list of digits that must have at least `i` elements, `b` is a list of digits where the first half of the elements are the maximum and minimum of the original elements of `a` and `b` respectively, and the second half of the elements are the minimum and maximum of the original elements of `a` and `b` respectively, `i` is equal to the length of `a`, and all elements of the list `a` are printed
    print()
    #This is printed: All elements of the list a
    for i in range(len(b)):
        print(b[i], end='')
        
    #State: `a` is a list of digits that must have at least `i` elements, `b` is a list of digits where the first half of the elements are the maximum and minimum of the original elements of `a` and `b` respectively, and the second half of the elements are the minimum and maximum of the original elements of `a` and `b` respectively, `i` is equal to the length of `b`, all elements of the list `a` are printed, nothing is printed, and all elements of the list `b` are printed.
    print()
    #This is printed: Nothing

#Overall this is what the function does:This function takes two strings of digits as input, swaps the maximum and minimum digits in the first half of the strings and the minimum and maximum digits in the second half, and then prints the modified strings. The function does not return any value, but instead prints the modified strings to the console.

