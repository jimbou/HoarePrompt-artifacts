#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^4) — the number of test cases. Each of the following t lines contains two integers x and y (0 <= x, y <= 10^9, x != y) — the parameters of the sequences.
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
        
    #State: n is an integer, m is an integer, k is a non-negative integer equal to the absolute difference between n and m, i is equal to the number of test cases t, stdin is empty. If the absolute difference between n and m (k) is a power of 2, then k is printed. Otherwise, if n is 0 and m is odd, the number 1 is printed. If n is 0 and m is even, the number 2 is printed. Otherwise, the value of k minus 2 to the power of p-1 is printed, where p is the number of digits in the binary representation of k.

#Overall this is what the function does:This function reads multiple lines of input from stdin, where the first line contains the number of test cases, and each subsequent line contains two integers. It calculates the absolute difference between the two integers and prints a value based on the following rules: if the difference is a power of 2, it prints the difference; if the first integer is 0 and the second is odd, it prints 1; if the first integer is 0 and the second is even, it prints 2; otherwise, it prints the difference minus 2 to the power of the number of digits in the binary representation of the difference minus 1. The function processes all test cases and leaves stdin empty.

