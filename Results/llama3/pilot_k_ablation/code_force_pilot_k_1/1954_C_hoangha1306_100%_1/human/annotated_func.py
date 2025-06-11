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
        
    #State: t is an integer between 1 and 1000 (inclusive), stdin is empty, q is t-1, a is the last string of digits from 1 to 9, b is the last string of digits from 1 to 9, kq1 is a string containing alternating minimum and maximum digits from the last pair of strings, kq2 is a string containing alternating maximum and minimum digits from the last pair of strings, vt is 1 if the last pair of strings have at least one different digit, otherwise vt is 0, kq1 and kq2 have been printed for all pairs of strings.

#Overall this is what the function does:This function reads an integer t from standard input, followed by t pairs of strings of digits from 1 to 9. For each pair, it generates two new strings by alternating between the minimum and maximum digits of the pair, and prints these strings. The function repeats this process for all t pairs, leaving the standard input empty and printing the alternating minimum and maximum digit strings for each pair.

