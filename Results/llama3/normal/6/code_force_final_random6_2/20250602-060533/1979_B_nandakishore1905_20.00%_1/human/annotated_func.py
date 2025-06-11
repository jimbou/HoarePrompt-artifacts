#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains a single integer t (1 <= t <= 10^4) — the number of test cases. Each test case contains two integers x and y (0 <= x, y <= 10^9, x != y) — the parameters of the sequences.
    for i in range(int(input())):
        n, m = map(int, input().split())
        
        k = abs(n - m)
        
        if k & k - 1 == 0:
            print(k)
        elif n == 0 and m % 2 != 0:
            print(1)
        elif n == 0 and m % 2 == 0:
            print(2)
        else:
            l = bin(k).replace('0b', '')
            p = len(l)
            q = 2 ** (p - 1)
            print(k - q)
        
    #State: n is an integer, m is an integer, k is a non-negative integer equal to the absolute difference between n and m, i is equal to the number of test cases, stdin is empty. If k is a power of 2, the absolute difference between n and m which is k is printed. Otherwise, if n is 0 and m is odd, the number 1 is printed. If n is 0 and m is even, the number 2 is printed. Otherwise, the difference between k and 2 to the power of p-1 is printed, where p is the number of digits in the binary representation of k.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two integers x and y. It calculates the absolute difference k between x and y and prints a value based on the following conditions: if k is a power of 2, it prints k; if x is 0 and y is odd, it prints 1; if x is 0 and y is even, it prints 2; otherwise, it prints the difference between k and 2 to the power of p-1, where p is the number of digits in the binary representation of k. The function processes all test cases and leaves the standard input empty.

