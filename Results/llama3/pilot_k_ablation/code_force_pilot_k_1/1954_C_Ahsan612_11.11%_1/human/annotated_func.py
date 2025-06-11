#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by 2t lines, each containing a string of digits from 1 to 9. The strings on each pair of lines have the same length.
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
        
    #State: stdin is empty, `a` and `b` are empty lists, `new` and `new2` are empty lists, `mid` is 0, `i` is 0, and 2t strings of digits have been printed, where each string is the result of comparing the corresponding digits from the input strings.

#Overall this is what the function does:This function reads input from stdin, where the input consists of an integer t followed by 2t lines of strings of digits. It then compares the corresponding digits from each pair of strings, printing two new strings for each pair: one with the maximum digit at each position in the first half and the minimum digit at each position in the second half, and another with the minimum digit at each position in the first half and the maximum digit at each position in the second half. The function repeats this process t times, emptying the stdin and leaving no residual data in the variables used.

