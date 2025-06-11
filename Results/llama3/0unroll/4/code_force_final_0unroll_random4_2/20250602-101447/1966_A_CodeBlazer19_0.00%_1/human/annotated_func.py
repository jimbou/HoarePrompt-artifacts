#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t test cases. Each test case consists of two lines. The first line contains two integers n and k (1 <= n <= 100, 2 <= k <= 100). The second line contains n integers c_1, c_2, ..., c_n (1 <= c_i <= 100).
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        print(k - 1)
        
    #State: The loop will print `t` lines, each containing the value `k - 1`, where `k` is the second integer in each test case. The value of `t` remains unchanged.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers (n and k) followed by a list of n integers. It then prints the value of k-1 for each test case, without modifying the input values. The function does not return any value, but instead prints the results directly to the console.

