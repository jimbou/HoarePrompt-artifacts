#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t pairs of integers x and y, where x and y are strings of the same length consisting of digits from 1 to 9.
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
        
    #State: Output State: a is a list of digits from the first pair of integers, where the first half of the digits are the maximum of the corresponding digits from the first and second pairs of integers, and the second half of the digits are the minimum of the corresponding digits from the first and second pairs of integers, b is a list of digits from the second pair of integers, where the first half of the digits are the minimum of the corresponding digits from the first and second pairs of integers, and the second half of the digits are the maximum of the corresponding digits from the first and second pairs of integers, stdin contains t-1 pairs of integers x and y, where x and y are strings of the same length consisting of digits from 1 to 9.
    for i in range(len(a)):
        print(a[i], end='')
        
    #State: Output State: The output state is a string of digits, where the first half of the digits are the maximum of the corresponding digits from the first and second pairs of integers, and the second half of the digits are the minimum of the corresponding digits from the first and second pairs of integers.
    print()
    #This is printed: The first half of the digits are the maximum of the corresponding digits from the first and second pairs of integers, and the second half of the digits are the minimum of the corresponding digits from the first and second pairs of integers.
    for i in range(len(b)):
        print(b[i], end='')
        
    #State: The output state is a string of digits, where the first half of the digits are the maximum of the corresponding digits from the first and second pairs of integers, and the second half of the digits are the minimum of the corresponding digits from the first and second pairs of integers
    print()
    #This is printed: (empty string)

#Overall this is what the function does:This function takes two pairs of integers as input, where each pair consists of two strings of the same length containing digits from 1 to 9. It then swaps the digits in the first half of each pair to be the maximum of the corresponding digits, and the digits in the second half to be the minimum of the corresponding digits. The function prints the modified first pair of integers, followed by the modified second pair of integers.

