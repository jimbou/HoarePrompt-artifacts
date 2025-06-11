#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing three integers n, a, and b (1 <= n <= 100, 1 <= a, b <= 30).
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        s1 = n * a
        
        s2 = b * (n // 2) + n % 2 * a
        
        print(min(s1, s2))
        
    #State: n is an integer between 1 and 100, a is an integer between 1 and 30, b is an integer between 1 and 30, s1 is the product of n and a, s2 is the product of b and the integer division of n by 2 plus the product of a and the remainder of n divided by 2, stdin is empty, _ is t-1, and the minimum value between s1 and s2 is being printed, and the minimum value between the product of n and a and the product of b and the integer division of n by 2 plus the product of a and the remainder of n divided by 2 is printed, and the minimum value between s1 and s2 is printed, and the minimum value between s1 and s2 is printed, and so on, t times.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers: n, a, and b. It calculates two values, s1 and s2, based on these inputs, and prints the minimum of these two values. The function repeats this process for a number of test cases specified by the first integer read from standard input.

