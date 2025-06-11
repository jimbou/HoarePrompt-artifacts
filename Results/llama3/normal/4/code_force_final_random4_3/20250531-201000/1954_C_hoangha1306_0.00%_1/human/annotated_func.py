#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by 2t strings, each string consisting of digits from 1 to 9, with all strings having the same length.
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
        
    #State: t is an integer between 1 and 1000 (inclusive), q is equal to t, stdin is empty, a is a string consisting of digits from 1 to 9, b is a string consisting of digits from 1 to 9, i is equal to the length of a, kq1 is a string consisting of digits from 1 to 9, kq2 is a string consisting of digits from 1 to 9, vt is 1, x is the minimum of the integer at index i-1 of a and b, y is the maximum of the integer at index i-1 of a and b, kq1 is printed, and kq2 is printed.

#Overall this is what the function does:This function reads input from stdin, where the first line contains an integer t (1 <= t <= 1000) followed by 2t strings, each consisting of digits from 1 to 9, with all strings having the same length. It then processes these strings in pairs, comparing corresponding characters and generating two new strings (kq1 and kq2) based on the comparison. The function prints these two strings for each pair of input strings. The function does not return any value, and its purpose is to generate and print the processed strings according to the specified rules.

