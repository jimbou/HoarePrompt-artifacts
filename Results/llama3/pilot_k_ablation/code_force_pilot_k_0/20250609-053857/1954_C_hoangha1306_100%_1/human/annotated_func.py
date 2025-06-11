#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t pairs of integers x and y, where x and y are non-negative integers of the same length, consisting only of digits from 1 to 9.
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
        
    #State: The output state is a series of pairs of integers, where each pair consists of two numbers that are the result of comparing corresponding digits of the input pairs. The comparison is done in a way that the smaller digit is assigned to the first number and the larger digit is assigned to the second number, but with a twist: if the digits are different, the assignment is swapped in every other iteration. The output state has the same number of pairs as the initial state, but with the modified digits.

#Overall this is what the function does:This function takes an integer t as input, representing the number of pairs of integers to process. For each pair, it compares corresponding digits and assigns the smaller digit to the first number and the larger digit to the second number, but with a twist: if the digits are different, the assignment is swapped in every other iteration. The function then prints the modified pairs of integers, with the same number of pairs as the initial input.

