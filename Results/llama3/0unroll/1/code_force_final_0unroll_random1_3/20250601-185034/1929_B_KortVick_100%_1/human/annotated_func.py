#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two space-separated integers: n and k, where n is a positive integer and k is a positive integer such that 1 <= k <= 4n - 2.
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        if 4 * n - 2 == k:
            print(k // 2 + 1)
        else:
            print(ceil(k / 2))
        
    #State: The output state will be the number of lines equal to the value of `t`, where each line contains an integer. If `k` is equal to `4n - 2`, the integer on that line will be `k // 2 + 1`. Otherwise, the integer on that line will be the ceiling of `k / 2`.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of two positive integers, n and k, and outputs the number of lines equal to the number of test cases. For each test case, if k is equal to 4n - 2, it prints k // 2 + 1; otherwise, it prints the ceiling of k / 2.

