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
                    if a[i] > b[i]:
                        kq1 = kq1 + str(x)
                        kq2 = kq2 + str(y)
                    else:
                        kq1 = kq1 + str(y)
                        kq2 = kq2 + str(x)
                else:
                    kq1 = kq1 + str(y)
                    kq2 = kq2 + str(x)
        
        print(kq1)
        
        print(kq2)
        
    #State: The loop will print 2t strings, where each pair of strings consists of the same digits, but with the first occurrence of a mismatched digit swapped. The remaining digits are appended in the order they appear in the original strings. The value of t remains unchanged.

#Overall this is what the function does:This function reads an integer t from standard input, representing the number of test cases. For each test case, it reads two strings of digits a and b of the same length. It then generates two new strings, kq1 and kq2, by comparing the digits of a and b from left to right. When a mismatch is found, the function swaps the mismatched digits in kq1 and kq2, and appends the remaining digits in the order they appear in the original strings. The function prints the resulting strings kq1 and kq2 for each test case.

