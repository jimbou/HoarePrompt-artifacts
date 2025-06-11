#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three space-separated integers a, b, and c, where a, b, and c are non-negative integers.
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
        
    #State: n is 0, i is n, a is a non-negative integer, b is a non-negative integer, c is a non-negative integer, stdin contains no test cases. If b % 3 != 0 and b % 3 + c < 3, then -1 is printed. Otherwise, k is a + (b + c) // 3 if (b + c) is divisible by 3, otherwise k is a + (b + c) // 3 + 1, and the value of k is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three non-negative integers a, b, and c. It then calculates a value k based on the values of a, b, and c. If b is not divisible by 3 and the sum of b and c is less than 3, it prints -1. Otherwise, it prints the value of k, which is a plus the integer division of (b + c) by 3, plus 1 if (b + c) is not divisible by 3. The function processes all test cases and prints the corresponding values of k or -1.

