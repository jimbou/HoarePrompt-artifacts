#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by 2t lines, each containing an integer x or y (1 <= x, y < 10^100) consisting only of digits from 1 to 9, and the length of x is equal to the length of y.
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
        
    #State: Output State: The output state will contain 2t lines, each containing an integer. The integers are the results of the comparisons and concatenations performed in the loop. The first t lines will contain the smaller of the two input integers at each position where they differ, and the second t lines will contain the larger of the two input integers at each position where they differ. The remaining positions will contain the same digit from both input integers.

#Overall this is what the function does:This function compares two input integers of equal length, digit by digit, and generates two output integers. The first output integer contains the smaller digit at each position where the input integers differ, and the same digit where they are the same. The second output integer contains the larger digit at each position where the input integers differ, and the same digit where they are the same. The function repeats this process for a specified number of test cases, each with two input integers.

