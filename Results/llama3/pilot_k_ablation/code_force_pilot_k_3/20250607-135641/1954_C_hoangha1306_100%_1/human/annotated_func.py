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
        
    #State: t is an integer between 1 and 1000 (inclusive), q is equal to t, stdin contains 0 pairs of integers x and y, a is a string of input, b is a string of input, i is equal to the length of the initial string a, kq1 is a string containing the characters of a and b in an alternating pattern of minimum and maximum integer values, kq2 is a string containing the characters of a and b in an alternating pattern of maximum and minimum integer values, vt is 1, and kq1 and kq2 are not being printed.

#Overall this is what the function does:This function reads a series of pairs of strings from standard input, where each string consists of digits from 1 to 9 and has the same length as its pair. For each pair, it generates two new strings by alternating between the minimum and maximum digit values at each position, starting with the minimum value for the first pair and the maximum value for the second pair. The function then prints these two strings. The process is repeated for the number of pairs specified by the first integer read from standard input, which is between 1 and 1000 (inclusive).

