#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by 2t lines, each containing an integer x or y (1 <= x, y < 10^100) consisting only of digits from 1 to 9, and the length of x is equal to the length of y.
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
        
    #State: _ is t, stdin is empty, and the maximum digits from the two input numbers are printed as a concatenated string for each iteration of the loop.

#Overall this is what the function does:This function reads input from stdin, where the first line contains an integer t, followed by 2t lines of integers x and y. It then compares the digits of x and y, and for each pair of digits, it prints the maximum digit in one line and the minimum digit in another line, repeating this process t times. The function does not return any value but prints the results to the console, leaving stdin empty after execution.

