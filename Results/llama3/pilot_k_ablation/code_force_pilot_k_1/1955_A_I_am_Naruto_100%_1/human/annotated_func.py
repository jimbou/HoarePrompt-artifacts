#State of the program right berfore the function call: stdin contains t+1 lines of input, where t is an integer (1 <= t <= 10^4). The first line contains t. Each of the remaining t lines contains three integers n, a, and b (1 <= n <= 100, 1 <= a, b <= 30).
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        s1 = n * a
        
        s2 = b * (n // 2) + n % 2 * a
        
        print(min(s1, s2))
        
    #State: stdin contains at least 1 line of input, n is an integer, a is an integer, b is an integer, s1 is an integer equal to n times a, s2 is an integer equal to b times the integer division of n by 2 plus a times the remainder of n divided by 2, the minimum value between s1 and s2 has been printed t times.

#Overall this is what the function does:This function reads a series of input lines from stdin, where the first line contains the number of test cases (t), and each subsequent line contains three integers (n, a, b). For each test case, it calculates two values (s1 and s2) based on the input integers and prints the minimum of these two values. The function repeats this process t times, printing the minimum value for each test case.

