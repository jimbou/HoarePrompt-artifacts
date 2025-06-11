#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^4). Each of the following t lines contains three integers n, a, and b (1 <= n, a, b <= 10^9).
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print(b * k - k * (k - 1) // 2 + (n - k) * a)
        
    #State: The loop has executed for the number of times specified by the input t, and the output state is the same as the output state after the loop executes 3 times, with the only difference being that the loop has executed for all the iterations specified by the input t.

#Overall this is what the function does:This function reads a series of input lines from standard input, where the first line contains an integer t, representing the number of test cases. For each test case, it reads three integers n, a, and b, and calculates the minimum cost by either multiplying a with n or using a formula involving a, b, and k (the minimum of n and b-a). It then prints the calculated cost for each test case. The function repeats this process for the number of test cases specified by the input t, producing a separate output for each case.

