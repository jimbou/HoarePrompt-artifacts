#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing two integers a and b (1 <= a, b <= 10^9).
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        if a % 2 == 0 or b % 2 == 0:
            if a % 2 == 0:
                a1, a2 = a // 2, a // 2
                if a1 != b:
                    print('Yes')
                    continue
            if b % 2 == 0:
                b1, b2 = b // 2, b // 2
                if b1 != a:
                    print('Yes')
                    continue
            print('No')
        else:
            print('No')
        
    #State: `_` is equal to `t`, stdin is empty.

#Overall this is what the function does:This function reads a series of pairs of integers from standard input, checks if either integer is even, and if so, checks if the other integer is equal to half of the even integer. If this condition is met, it prints 'Yes', otherwise it prints 'No'. The function continues this process until all input pairs have been processed, at which point the standard input is empty.

