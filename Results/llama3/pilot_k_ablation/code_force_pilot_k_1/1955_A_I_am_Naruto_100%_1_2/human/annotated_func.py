#State of the program right berfore the function call: stdin contains t+1 inputs: first an integer t (1 <= t <= 10^4) and then t lines each containing three integers n, a, and b (1 <= n <= 100, 1 <= a, b <= 30).
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        s1 = n * a
        
        s2 = b * (n // 2) + n % 2 * a
        
        print(min(s1, s2))
        
    #State: t is 0, stdin is empty, _ is t, n, a, and b are the last values read from stdin, s1 is n times a, s2 is b times the integer division of n by 2, plus a if n is odd, and the minimum of s1 and s2 has been printed t times.

#Overall this is what the function does:Reads a series of test cases from standard input, where each test case consists of three integers: n, a, and b. For each test case, it calculates two sums: s1 (n times a) and s2 (b times the integer division of n by 2, plus a if n is odd). It then prints the minimum of these two sums. This process is repeated for a number of test cases specified by the first integer read from standard input.

