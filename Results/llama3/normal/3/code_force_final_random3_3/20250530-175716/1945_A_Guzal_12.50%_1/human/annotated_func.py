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
        
    #State: n is an integer (1 <= n <= 10^4), i is n-1, a, b, c are integers (0 <= a, b, c <= 10^9), k is an integer. If (b % 3 != 0 and c < 3) and (b + c) % 3 != 0, then -1 is printed. Otherwise, if (b + c) % 3 != 0, then k is a + (b + c) // 3 + 1 and the value of k is printed. If (b + c) % 3 == 0, then k is a + (b + c) // 3 and the value of k is printed.

#Overall this is what the function does:This function reads an integer t from standard input, representing the number of test cases, and then for each test case, it reads three integers a, b, and c. It calculates a value k based on the values of a, b, and c, and prints the result. If (b % 3 != 0 and c < 3) and (b + c) % 3 != 0, it prints -1. Otherwise, it calculates k as a + (b + c) // 3, and if (b + c) % 3 != 0, it increments k by 1. The function repeats this process for all test cases.

