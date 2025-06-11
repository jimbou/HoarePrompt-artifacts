#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t pairs of integers x and y, where x and y are non-negative integers consisting only of digits from 1 to 9 and have the same length.
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
        
    #State: Output State: The first half of the list a contains the maximum values from the corresponding pairs of integers from stdin, and the second half of the list a contains the minimum values from the corresponding pairs of integers from stdin. The first half of the list b contains the minimum values from the corresponding pairs of integers from stdin, and the second half of the list b contains the maximum values from the corresponding pairs of integers from stdin.
    for i in range(len(a)):
        print(a[i], end='')
        
    #State: Output State: The first half of the list a contains the maximum values from the corresponding pairs of integers from stdin, and the second half of the list a contains the minimum values from the corresponding pairs of integers from stdin. The first half of the list b contains the minimum values from the corresponding pairs of integers from stdin, and the second half of the list b contains the maximum values from the corresponding pairs of integers from stdin.
    print()
    #This is printed: The first half of the list a contains the maximum values from the corresponding pairs of integers from stdin, and the second half of the list a contains the minimum values from the corresponding pairs of integers from stdin. The first half of the list b contains the minimum values from the corresponding pairs of integers from stdin, and the second half of the list b contains the maximum values from the corresponding pairs of integers from stdin.
    for i in range(len(b)):
        print(b[i], end='')
        
    #State: Output State: The first half of the list a contains the maximum values from the corresponding pairs of integers from stdin, and the second half of the list a contains the minimum values from the corresponding pairs of integers from stdin. The list b is printed in its entirety, with the minimum values from the corresponding pairs of integers from stdin in the first half and the maximum values from the corresponding pairs of integers from stdin in the second half.
    print()
    #This is printed: a newline character

#Overall this is what the function does:The function takes two pairs of integers from standard input, swaps the maximum and minimum values in the first half and second half of each pair, and prints the modified pairs. The first pair is printed with the maximum values in the first half and the minimum values in the second half, followed by the second pair printed in its entirety with the minimum values in the first half and the maximum values in the second half.

