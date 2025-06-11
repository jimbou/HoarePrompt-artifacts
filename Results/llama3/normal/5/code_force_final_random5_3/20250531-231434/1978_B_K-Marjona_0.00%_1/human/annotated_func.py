#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers n, a, and b (1 <= n, a, b <= 10^9).
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print((b + (b - k + 1)) // 2 * k + (n - k) * a)
        
    #State: n is an integer equal to the first input, a is an integer equal to the second input, b is an integer equal to the third input, k is an integer equal to the minimum of n and b - a, _ is equal to the number of test cases, stdin is empty. If b is less than or equal to a, the program prints a*n where a is the second input and n is the first input. Otherwise, the program prints the sum of the k largest numbers from a to b, where k is the minimum of n and b - a, plus the product of the remaining n - k numbers and a.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case contains three integers: n, a, and b. For each test case, it calculates and prints the sum of the k largest numbers from a to b, where k is the minimum of n and b - a, plus the product of the remaining n - k numbers and a, if b is greater than a. If b is less than or equal to a, it simply prints the product of a and n. After processing all test cases, the function leaves the standard input empty.

