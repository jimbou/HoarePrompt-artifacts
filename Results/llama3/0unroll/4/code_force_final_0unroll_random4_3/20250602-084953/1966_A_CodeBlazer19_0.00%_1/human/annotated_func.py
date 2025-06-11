#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t test cases. Each test case consists of two lines. The first line contains two integers n and k (1 <= n <= 100, 2 <= k <= 100). The second line contains n integers c_1, c_2, ..., c_n (1 <= c_i <= 100).
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        print(k - 1)
        
    #State: Output State: The program will print the value of `k - 1` for each test case, where `k` is the second integer in the first line of each test case. The value of `t` remains unchanged, and the values of `n` and `c_i` are not used in the loop body.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two lines. The first line contains two integers, and the function prints the second integer minus one for each test case. The function does not modify the input values or use the first integer and the subsequent integers in the second line of each test case.

