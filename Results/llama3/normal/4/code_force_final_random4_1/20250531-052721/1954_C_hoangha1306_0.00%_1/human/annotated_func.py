#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by 2t strings, each representing an integer consisting only of digits from 1 to 9, with the first t strings having the same length as the next t strings.
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
        
    #State: t is an integer (1 <= t <= 1000), stdin contains 0 strings, q is t, a is an empty string, b is an empty string, kq1 is a string representing the digits of a and b in a specific order, kq2 is a string representing the digits of a and b in a specific order, vt is 0 or 1, and i is equal to the length of a, and kq2 (a string representing the digits of a and b in a specific order) is printed

#Overall this is what the function does:This function takes an integer t (1 <= t <= 1000) and 2t strings from standard input, where the first t strings have the same length as the next t strings. It then compares the corresponding characters of each pair of strings, and for each pair, it constructs two new strings: one with the smaller character at the first mismatch and the larger character at the second mismatch, and another with the larger character at the first mismatch and the smaller character at the second mismatch. The function prints these two strings for each pair of input strings.

