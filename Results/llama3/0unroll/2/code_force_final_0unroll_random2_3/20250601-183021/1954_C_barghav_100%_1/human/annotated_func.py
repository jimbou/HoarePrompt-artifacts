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
        
    #State: Output State: a contains the digits of the maximum integer that can be formed using the digits of the first pair's x and y, b contains the digits of the minimum integer that can be formed using the digits of the first pair's x and y, f is 1.
    for i in range(len(a)):
        print(a[i], end='')
        
    #State: Output State: a contains the digits of the maximum integer that can be formed using the digits of the first pair's x and y, b contains the digits of the minimum integer that can be formed using the digits of the first pair's x and y, f is 1, and the console output is the digits of the maximum integer that can be formed using the digits of the first pair's x and y.
    print()
    #This is printed: The digits of the maximum integer that can be formed using the digits of the first pair's x and y
    for i in range(len(b)):
        print(b[i], end='')
        
    #State: Output State: a contains the digits of the maximum integer that can be formed using the digits of the first pair's x and y, b is empty, f is 1, and the console output is the digits of the maximum integer that can be formed using the digits of the first pair's x and y, followed by the digits of the minimum integer that can be formed using the digits of the first pair's x and y.
    print()
    #This is printed: the digits of the maximum integer that can be formed using the digits of the first pair's x and y, followed by the digits of the minimum integer that can be formed using the digits of the first pair's x and y

#Overall this is what the function does:This function reads two pairs of integers from standard input, compares the digits of the first pair, and prints the maximum and minimum integers that can be formed using the digits of the first pair. It does not return any value but modifies the console output.

