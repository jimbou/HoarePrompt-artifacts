#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^3). Each of the following t lines contains two integers n and k (1 <= n <= 100, 0 <= k <= n*(n-1)/2).
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n)
        
    #State: The output state will be a list of t integers, where each integer is either 1 or n, depending on the value of k. If k is greater than or equal to n-1, the output will be 1, otherwise it will be n.

#Overall this is what the function does:This function reads a series of input lines from standard input, where the first line contains the number of test cases (t) and each subsequent line contains two integers (n and k). It then prints a list of t integers, where each integer is either 1 or n, depending on whether k is greater than or equal to n-1. If k is greater than or equal to n-1, the output is 1; otherwise, the output is n. The function does not modify the input values and only produces output based on the conditions specified.

