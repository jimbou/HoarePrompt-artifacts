#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by 2t lines, each containing a string of digits from 1 to 9. Each pair of strings has the same length.
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
        
    #State: a is a list of integers where each element is a string of digits from 1 to 9, b is a list of integers where each element is a string of digits from 1 to 9, new is a list of integers where each element is the minimum of the corresponding elements of a and b, new2 is a list of integers where each element is the maximum of the corresponding elements of a and b, i is equal to the length of a, stdin contains 0 lines, and a string of digits formed by concatenating the elements of the list new2 is being printed.

#Overall this is what the function does:This function reads input from stdin, where the first line contains an integer t, followed by 2t lines of strings of digits from 1 to 9. It then processes each pair of strings, comparing them digit by digit. If the strings are identical up to a certain point, it outputs two new strings: one with the maximum digit at each position and one with the minimum digit at each position. If the strings differ at some point, it outputs two new strings: one with the minimum digit at each position up to the point of difference and the maximum digit at each position thereafter, and one with the maximum digit at each position up to the point of difference and the minimum digit at each position thereafter. The function repeats this process t times, printing the resulting strings to stdout.

