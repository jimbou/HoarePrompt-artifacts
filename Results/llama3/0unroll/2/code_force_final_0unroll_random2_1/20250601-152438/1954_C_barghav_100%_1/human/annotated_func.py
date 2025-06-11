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
        
    #State: Output State: a is a list of digits from the first pair of integers, b is a list of digits from the second pair of integers, f is 1, stdin contains t-1 pairs of integers x and y, where x and y are strings of digits from 1 to 9 and have the same length.
    for i in range(len(a)):
        print(a[i], end='')
        
    #State: Output State: The output state is a list of digits from the first pair of integers, b is a list of digits from the second pair of integers, f is 1, stdin contains t-1 pairs of integers x and y, where x and y are strings of digits from 1 to 9 and have the same length, and the console output is the string of digits from the first pair of integers.
    print()
    #This is printed: Nothing
    for i in range(len(b)):
        print(b[i], end='')
        
    #State: Output State: The output state is a list of digits from the first pair of integers, b is a list of digits from the second pair of integers, f is 1, stdin contains t-1 pairs of integers x and y, where x and y are strings of digits from 1 to 9 and have the same length, and the console output is the string of digits from the first pair of integers followed by the string of digits from the second pair of integers.
    print()
    #This is printed: the string of digits from the first pair of integers followed by the string of digits from the second pair of integers

#Overall this is what the function does:This function reads two pairs of integers from standard input, compares and swaps them if necessary, and then prints the first pair of integers followed by the second pair of integers. The function does not return any value, but it modifies the standard input by consuming the first pair of integers. The function's purpose is to output the two pairs of integers in a specific order, with the first pair being the one that is lexicographically smaller or equal to the second pair.

