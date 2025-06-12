#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t pairs of integers x and y, where x and y are non-negative integers consisting only of digits from 1 to 9 and have the same number of digits.
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
        
    #State: t is an integer between 1 and 1000, stdin is empty, q is t-1, a is a string containing the last pair of integers x and y, b is a string containing the last pair of integers x and y, kq1 is a string containing the last pair of integers x and y where each character is either equal to the corresponding character in a or the minimum/maximum of the integer values of the corresponding characters in a and b, kq2 is a string containing the last pair of integers x and y where each character is either equal to the corresponding character in a or the maximum/minimum of the integer values of the corresponding characters in a and b, vt is either 0 or 1 depending on whether the loop executed at least once and found a mismatch between a and b, and t pairs of strings kq1 and kq2 are printed (where kq1 and kq2 are strings containing pairs of integers x and y where each character is either equal to the corresponding character in a or the minimum/maximum of the integer values of the corresponding characters in a and b)

#Overall this is what the function does:This function reads input from stdin, expecting an integer t followed by t pairs of integers x and y, where x and y are non-negative integers consisting only of digits from 1 to 9 and have the same number of digits. It then generates two new pairs of integers, kq1 and kq2, by comparing each digit of x and y. If the digits are equal, the corresponding digit in kq1 and kq2 is the same as in x and y. If the digits are different, the digit in kq1 is the minimum of the two digits, and the digit in kq2 is the maximum of the two digits, but with a twist: if a mismatch is found, the function toggles between using the minimum and maximum for subsequent mismatches. The function prints each pair of kq1 and kq2, resulting in t pairs of strings being printed.

