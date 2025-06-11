#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by 2t lines, each containing a string of digits from 1 to 9, such that the strings on each pair of lines have the same length.
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
        
    #State: a is a list of digits, b is a list of digits, f is 1, stdin contains t-1 pairs of strings of digits, each pair having the same length.
    for i in range(len(a)):
        print(a[i], end='')
        
    #State: The list 'a' has been printed to the console, with each digit separated by a space, and the value of 'i' is equal to the length of 'a'.
    print()
    #This is printed: an empty line
    for i in range(len(b)):
        print(b[i], end='')
        
    #State: Output State: The list 'b' has been printed to the console, with each digit separated by no space, and the value of 'i' is equal to the length of 'b', and a blank line is printed.
    print()
    #This is printed: a blank line

#Overall this is what the function does:This function reads two lines of digits from standard input, compares and swaps them if necessary to ensure the first line is lexicographically larger, then prints the first line with digits separated by spaces, followed by the second line with digits separated by no spaces, and finally prints a blank line.

