#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 1000). Each of the following t lines contains two integers n and k (2 <= n <= 10^8, 1 <= k <= 4n - 2).
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        if k == 1:
            print(1)
            continue
        
        if k <= 2 * (n + (n - 2)):
            print(math.ceil(k / 2))
        else:
            print(k // 2 + 1)
        
    #State: The output will be the number of operations required to make all elements of the array equal, for each test case. The output will be a series of integers, each on a new line, representing the minimum number of operations required for each test case.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two integers n and k. It then calculates and prints the minimum number of operations required to make all elements of an array equal, for each test case. The output is a series of integers, each on a new line, representing the minimum number of operations required for each test case.

