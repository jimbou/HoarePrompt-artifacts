#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two distinct non-negative integers x and y, separated by a space.
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
        
    #State: n is an integer, m is an integer, k is the absolute difference between n and m, i is equal to the number of test cases, stdin is empty. If the absolute difference between n and m which is k is a power of 2, then k is printed for each test case. Otherwise, if n is 0 and m is odd, the number 1 is printed for each test case. If n is 0 and m is even, the number 2 is printed for each test case. Otherwise, the difference between k and 2 to the power of p-1 is printed for each test case, where p is the number of digits in the binary representation of k.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains two distinct non-negative integers. For each test case, it calculates the absolute difference between the two integers and prints a value based on the following conditions: if the absolute difference is a power of 2, it prints the absolute difference; if the first integer is 0 and the second integer is odd, it prints 1; if the first integer is 0 and the second integer is even, it prints 2; otherwise, it prints the difference between the absolute difference and 2 to the power of the number of digits in the binary representation of the absolute difference minus 1. After processing all test cases, the function leaves the standard input empty.

