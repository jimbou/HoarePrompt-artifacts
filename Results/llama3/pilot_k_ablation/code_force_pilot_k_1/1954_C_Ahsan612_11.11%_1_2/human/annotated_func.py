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
        
    #State: stdin is empty, _ is equal to the value of t, a and b are empty lists, new and new2 are empty lists, mid is 0, i is 0, and 2t strings of digits are printed where each digit is the maximum of the corresponding digits in the input pairs and the minimum of the corresponding digits in the input pairs.

#Overall this is what the function does:This function reads input from stdin, processes pairs of strings of digits, and prints two strings for each pair. The first string contains the maximum digit from each corresponding pair of digits in the input strings, and the second string contains the minimum digit from each corresponding pair of digits in the input strings. The function repeats this process for a number of pairs specified by the first integer input, leaving stdin empty after execution.

