#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by 2t lines. Each pair of lines contains two integers x and y of the same length, consisting of digits from 1 to 9.
    for _ in range(int(input())):
        a = list(map(int, list(input())))
        
        b = list(map(int, list(input())))
        
        new = [None] * len(a)
        
        new2 = [None] * len(a)
        
        i = 0
        
        while i < len(a) and a[i] == b[i]:
            new[i] = max(a[i], b[i])
            new2[i] = min(a[i], b[i])
            i += 1
        
        if i != len(a):
            new[i] = max(a[i], b[i])
            new2[i] = min(a[i], b[i])
            i += 1
            while i < len(a):
                new[i] = min(a[i], b[i])
                new2[i] = max(a[i], b[i])
                i += 1
        
        print(''.join(str(x) for x in new))
        
        print(''.join(str(x) for x in new2))
        
    #State: a is a list of integers, b is a list of integers where all elements are equal to the corresponding elements of a, new is a list of integers where all elements are the minimum of the corresponding elements of a and b, new2 is a list of integers where all elements are the maximum of the corresponding elements of a and b, i is equal to len(a), and stdin contains 0 lines.

#Overall this is what the function does:This function reads input from stdin, where the first line contains an integer t, followed by 2t lines of integers. It then processes each pair of lines, comparing the integers digit by digit. If the digits are equal, it outputs the maximum digit; otherwise, it outputs the minimum digit for the first differing digit and then swaps the output for the remaining digits. The function repeats this process t times, printing the resulting integers for each pair of input lines.

