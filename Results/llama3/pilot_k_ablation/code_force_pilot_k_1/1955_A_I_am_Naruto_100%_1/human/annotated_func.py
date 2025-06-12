#State of the program right berfore the function call: stdin contains t+1 inputs: the first input is an integer t (1 <= t <= 10^4), and each of the next t inputs is a line containing three integers n, a, and b (1 <= n <= 100, 1 <= a, b <= 30).
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        s1 = n * a
        
        s2 = b * (n // 2) + n % 2 * a
        
        print(min(s1, s2))
        
    #State: t is 0, stdin is empty, n, a, and b are the last set of inputs, s1 is the product of n and a, s2 is the sum of the product of b and the integer division of n by 2, and the product of a and the remainder of n divided by 2, _ is t.

#Overall this is what the function does:This function reads a series of inputs from standard input, where the first input is the number of test cases (t), and each subsequent input is a set of three integers (n, a, and b). For each set of inputs, it calculates two sums: s1, the product of n and a, and s2, the sum of the product of b and the integer division of n by 2, and the product of a and the remainder of n divided by 2. It then prints the minimum of these two sums. The function continues this process until all test cases have been processed, at which point standard input is empty.

