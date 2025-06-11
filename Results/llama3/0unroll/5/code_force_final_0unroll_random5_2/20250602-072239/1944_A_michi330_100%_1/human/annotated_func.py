#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^3). Each of the following t lines contains two integers n and k (1 <= n <= 100, 0 <= k <= n*(n-1)/2).
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n)
        
    #State: The output state will be a list of t integers, where each integer is either 1 or n, depending on the value of k for each iteration. If k is greater than or equal to n-1, the output will be 1; otherwise, the output will be n.

#Overall this is what the function does:This function reads input from stdin, expecting a specific format. It first reads an integer t, representing the number of test cases. For each test case, it reads two integers n and k. Based on the value of k, it prints either 1 or n. If k is greater than or equal to n-1, it prints 1; otherwise, it prints n. The function outputs a list of t integers, where each integer corresponds to the result of each test case.

