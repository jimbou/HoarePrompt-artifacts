#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by 2t integers x and y, where x and y are non-negative integers consisting only of digits from 1 to 9 and have the same number of digits.
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
        
    #State: The output state will contain 2t strings, each representing the maximum and minimum possible numbers that can be formed by comparing the corresponding digits of the input numbers x and y. The comparison starts from the most significant digit and continues until a mismatch is found. After the mismatch, the remaining digits are compared in reverse order. The resulting strings will have the same number of digits as the input numbers.

#Overall this is what the function does:This function reads input from stdin, where the first line contains an integer t, representing the number of test cases. For each test case, it reads two non-negative integers x and y, consisting only of digits from 1 to 9 and having the same number of digits. It then generates two new numbers by comparing the corresponding digits of x and y. The comparison starts from the most significant digit and continues until a mismatch is found. After the mismatch, the remaining digits are compared in reverse order. The function prints the maximum and minimum possible numbers that can be formed by this comparison, one per line, for each test case.

