#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by 2t lines, where each pair of lines contains two integers x and y of the same length, consisting of digits from 1 to 9.
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
        
    #State: t is an integer between 1 and 1000, stdin is empty, q is t, a and b are empty strings, kq1 and kq2 are empty strings, vt is 0 if all pairs of corresponding digits in all pairs of input strings are equal, and vt is 1 if there is at least one pair of corresponding digits in any pair of input strings that are not equal, and 2t strings have been printed, each string containing the smaller digit from each pair of corresponding digits in a pair of input strings if all pairs of corresponding digits in that pair are equal, and the larger digit from each pair of corresponding digits in a pair of input strings if there is at least one pair of corresponding digits in that pair that are not equal, and the larger digit from each pair of corresponding digits in a pair of input strings if all pairs of corresponding digits in that pair are equal, and the smaller digit from each pair of corresponding digits in a pair of input strings if there is at least one pair of corresponding digits in that pair that are not equal.

#Overall this is what the function does:This function reads input from stdin, processes pairs of strings of equal length consisting of digits from 1 to 9, and prints two strings for each pair. If all pairs of corresponding digits in a pair are equal, it prints the smaller digit from each pair. If there is at least one pair of corresponding digits that are not equal, it prints the larger digit from each pair. The function repeats this process for a specified number of test cases (t) and then empties the stdin.

