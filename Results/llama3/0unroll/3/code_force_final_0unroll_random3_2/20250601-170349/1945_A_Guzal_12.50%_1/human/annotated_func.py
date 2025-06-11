#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing three integers a, b, c (0 <= a, b, c <= 10^9).
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        k = 0
        
        if (b % 3 != 0 and c < 3) and (b + c) % 3 != 0:
            print(-1)
        else:
            k += a + (b + c) // 3
            if (b + c) % 3 != 0:
                k += 1
            print(k)
        
    #State: The output state will contain `n` lines, each containing an integer. The integer on each line will be the calculated value of `k` for the corresponding input values of `a`, `b`, and `c`. The value of `k` is calculated as `a` plus the integer division of `b + c` by 3, plus 1 if the remainder of `b + c` divided by 3 is not 0. If the conditions `(b % 3 != 0 and c < 3) and (b + c) % 3 != 0` are met, the output will be -1 instead. The values of `n`, `a`, `b`, and `c` will remain unchanged.

#Overall this is what the function does:Calculates and prints the value of `k` for each set of input integers `a`, `b`, and `c`, where `k` is determined by the sum of `a` and the integer division of `b + c` by 3, with an additional 1 added if the remainder of `b + c` divided by 3 is not 0, unless the conditions `(b % 3 != 0 and c < 3) and (b + c) % 3 != 0` are met, in which case the output is -1.

