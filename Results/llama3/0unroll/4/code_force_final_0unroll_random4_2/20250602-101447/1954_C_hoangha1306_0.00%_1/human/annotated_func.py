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
        
    #State: Output State: The output state will be a series of pairs of integers, where each pair consists of two integers that are the result of comparing the corresponding digits of the input pairs. The comparison is done in a way that the smaller digit is always placed in the first integer of the pair, and the larger digit is always placed in the second integer of the pair. If the digits are equal, they are placed in both integers of the pair. The output state will have the same number of pairs as the input state, and each pair will have the same number of digits as the input pairs.

#Overall this is what the function does:This function reads input from stdin, processes pairs of integers, and prints pairs of integers as output. It takes no parameters and returns no value. The function reads an integer t, representing the number of pairs to process, followed by t pairs of integers x and y. For each pair, it compares the corresponding digits of x and y, placing the smaller digit in the first integer of the output pair and the larger digit in the second integer. If the digits are equal, they are placed in both integers of the output pair. The function prints each output pair on separate lines. The output state consists of a series of pairs of integers, with the same number of pairs and digits as the input state.

