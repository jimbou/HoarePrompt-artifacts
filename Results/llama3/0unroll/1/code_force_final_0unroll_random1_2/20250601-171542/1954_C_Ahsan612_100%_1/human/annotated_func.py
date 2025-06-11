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
        
    #State: The output state contains 2t lines. Each pair of lines contains two integers of the same length as the input integers, consisting of digits from 1 to 9. The first integer in each pair is the maximum of the corresponding digits in the input integers, and the second integer is the minimum of the corresponding digits in the input integers. If the input integers are identical, the output integers are also identical. If the input integers differ, the first differing digit is set to the maximum of the two digits, and the remaining digits are set to the minimum of the two digits.

#Overall this is what the function does:This function reads pairs of integers from standard input, compares them digit by digit, and prints two new integers for each pair. The first integer in each pair is the maximum of the corresponding digits in the input integers, and the second integer is the minimum of the corresponding digits in the input integers. If the input integers are identical, the output integers are also identical. If the input integers differ, the first differing digit is set to the maximum of the two digits, and the remaining digits are set to the minimum of the two digits. The function repeats this process for a number of pairs specified by the first integer read from standard input.

