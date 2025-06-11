#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by 2t lines, each containing an integer x (1 <= x < 10^100) and an integer y (1 <= y < 10^100), where x and y consist only of digits from 1 to 9 and have the same length.
    for _ in range(int(input())):
        a = list(map(int, list(input())))
        
        b = list(map(int, list(input())))
        
        new = [None] * len(a)
        
        new2 = [None] * len(a)
        
        mid = len(a) // 2
        
        i = 0
        
        while i < mid:
            new[i] = max(a[i], b[i])
            new2[i] = min(a[i], b[i])
            i += 1
        
        while i < len(a):
            new[i] = min(a[i], b[i])
            new2[i] = max(a[i], b[i])
            i += 1
        
        print(''.join(str(x) for x in new))
        
        print(''.join(str(x) for x in new2))
        
    #State: a is a list of digits from the last input line with a length greater than 0, b is a list of digits from the last input line, new is a list of values with the same length as a, where all elements are the minimum of a[i] and b[i], new2 is a list of values with the same length as a, where all elements are the maximum of a[i] and b[i], mid is half the length of a, i is equal to the length of a, stdin contains 0 lines, _ is t - 1, and the list of minimum values between corresponding elements of a and b is printed as a string, and the list of maximum values between corresponding elements of a and b is printed as a string.

#Overall this is what the function does:This function reads input from stdin, where the first line contains an integer t, followed by 2t lines, each containing two integers x and y. It then processes each pair of integers by comparing their corresponding digits and printing the maximum and minimum values for the first half of the digits and the minimum and maximum values for the second half of the digits. The function repeats this process t times, printing the results as strings.

