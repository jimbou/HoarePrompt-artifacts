#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t pairs of integers x and y, where x and y are strings of digits from 1 to 9 and have the same length.
    t = int(input())
    for q in range(t):
        a = input()
        
        b = input()
        
        kq1 = ''
        
        kq2 = ''
        
        vt = 0
        
        for i in range(len(a)):
            if a[i] == b[i]:
                kq1 = kq1 + a[i]
                kq2 = kq2 + a[i]
                continue
            else:
                x, y = min(int(a[i]), int(b[i])), max(int(a[i]), int(b[i]))
                if vt == 0:
                    vt = 1
                    kq1 = kq1 + str(x)
                    kq2 = kq2 + str(y)
                else:
                    kq1 = kq1 + str(y)
                    kq2 = kq2 + str(x)
        
        print(kq1)
        
        print(kq2)
        
    #State: t is an integer greater than or equal to 1, q is equal to t, stdin is empty, a is a string of digits from 1 to 9, b is a string of digits from 1 to 9, i is equal to the length of a, kq1 is a string of digits from 1 to 9, kq2 is a string of digits from 1 to 9, vt is 1 if the length of a is odd, otherwise vt is 0, kq1 is printed, and kq2 is printed

#Overall this is what the function does:Functionality: This function reads an integer t from standard input, representing the number of test cases. For each test case, it reads two strings a and b of the same length, consisting of digits from 1 to 9. It then generates two new strings, kq1 and kq2, by comparing the corresponding digits of a and b. If the digits are the same, it appends the digit to both kq1 and kq2. If the digits are different, it appends the smaller digit to kq1 and the larger digit to kq2, but switches the order of the digits if the length of a is odd. Finally, it prints kq1 and kq2 for each test case.

