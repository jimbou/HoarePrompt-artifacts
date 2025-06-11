#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 10^4). Each of the following t lines contains three integers a, b, c (0 <= a, b, c <= 10^9).
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
        
    #State: Output State: The output will be n lines, each containing an integer k. The value of k is calculated based on the input values a, b, and c. If the conditions (b % 3 != 0 and c < 3) and (b + c) % 3 != 0 are met, the output will be -1. Otherwise, k will be the sum of a and the integer division of (b + c) by 3, plus 1 if (b + c) is not divisible by 3.

#Overall this is what the function does:Calculates and prints the value of k for each set of input integers a, b, and c, based on specific conditions, or outputs -1 if the conditions are not met.

