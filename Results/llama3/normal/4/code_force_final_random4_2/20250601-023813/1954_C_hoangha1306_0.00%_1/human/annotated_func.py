#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by 2t strings x and y, where x and y are of the same length and consist only of digits from 1 to 9.
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
        
    #State: t is an integer between 1 and 1000, q is equal to t, stdin is empty, a is an empty string, b is an empty string, kq1 and kq2 are strings consisting of the digits of the original a and b, but with the digits rearranged such that kq1 contains the smaller of the two digits at each position where a and b differ, and kq2 contains the larger of the two digits at each position where a and b differ, vt is either 0 or 1, kq1 is printed, and kq2 is printed

#Overall this is what the function does:This function reads input from stdin, where the first line contains an integer t (1 <= t <= 1000), followed by 2t strings x and y of the same length, consisting only of digits from 1 to 9. It then rearranges the digits of x and y such that at each position where x and y differ, the smaller digit is placed in kq1 and the larger digit is placed in kq2. The function prints kq1 and kq2 for each pair of input strings.

