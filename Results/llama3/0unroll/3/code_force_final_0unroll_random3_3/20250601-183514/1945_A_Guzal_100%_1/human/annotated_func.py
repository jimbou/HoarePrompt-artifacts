#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing three integers a, b, c (0 <= a, b, c <= 10^9).
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        k = 0
        
        if b % 3 != 0 and b % 3 + c < 3:
            print(-1)
        else:
            k += a + (b + c) // 3
            if (b + c) % 3 != 0:
                k += 1
            print(k)
        
    #State: The output state will contain n lines, each containing an integer. If the condition b % 3 != 0 and b % 3 + c < 3 is true for a line, the output will be -1. Otherwise, the output will be the sum of a, the integer division of (b + c) by 3, and 1 if (b + c) is not divisible by 3. The value of n remains unchanged.

#Overall this is what the function does:This function reads an integer t from standard input, representing the number of test cases. For each test case, it reads three integers a, b, and c, and calculates a value k. If b is not divisible by 3 and the sum of b and c is less than 3, it prints -1. Otherwise, it calculates k as the sum of a, the integer division of (b + c) by 3, and 1 if (b + c) is not divisible by 3. The function prints the calculated value k for each test case, resulting in a total of t output lines.

