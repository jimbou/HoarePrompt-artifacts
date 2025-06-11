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
        
    #State: n is an integer between 1 and 10^4, i is n-1, a, b, c are integers (0 <= a, b, c <= 10^9), k is a + (b + c) // 3 if (b + c) is divisible by 3, otherwise k is a + (b + c) // 3 + 1. If b % 3 != 0 and b % 3 + c < 3, then -1 is printed. Otherwise, stdin contains 0 lines, each containing three integers. If (b + c) % 3 != 0, then k is a + (b + c) // 3 + 1 if (b + c) is divisible by 3, otherwise k is a + (b + c) // 3 + 2. If b % 3 != 0 and b % 3 + c < 3, then -1 is being printed, and k is printed, where k is a + (b + c) // 3 if (b + c) is divisible by 3, otherwise k is a + (b + c) // 3 + 1.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers a, b, and c. For each test case, it calculates a value k based on the divisibility of (b + c) by 3. If (b + c) is divisible by 3, k is set to a + (b + c) // 3. If (b + c) is not divisible by 3, k is set to a + (b + c) // 3 + 1. However, if b is not divisible by 3 and the sum of b and c is less than 3, the function prints -1. Otherwise, it prints the calculated value of k. The function repeats this process for the specified number of test cases, leaving the input stream empty afterwards.

