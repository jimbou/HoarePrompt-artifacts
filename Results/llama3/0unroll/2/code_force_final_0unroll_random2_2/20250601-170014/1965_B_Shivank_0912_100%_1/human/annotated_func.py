#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing two integers n and k (2 <= n <= 10^6, 1 <= k <= n).
    t = int(input())
    for tc in range(t):
        n, k = map(int, input().split())
        
        i = 0
        
        while 1 << i + 1 <= k:
            i = i + 1
        
        ans = [k - (1 << i), k + 1, k + 1 + (1 << i)]
        
        for j in range(20):
            if j != i:
                ans.append(1 << j)
        
        print(len(ans))
        
        print(*ans)
        
    #State: The output state will contain `t` number of lines, each containing the length of the list `ans` and the elements of the list `ans` separated by spaces. The list `ans` will contain `k - (1 << i)`, `k + 1`, `k + 1 + (1 << i)`, and 20 binary numbers (powers of 2) excluding the binary number corresponding to the value of `i`. The value of `i` is the largest power of 2 that is less than or equal to `k`.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers n and k. For each test case, it generates a list of numbers, including k - (1 << i), k + 1, k + 1 + (1 << i), and 20 binary numbers (powers of 2) excluding the binary number corresponding to the value of i, where i is the largest power of 2 that is less than or equal to k. The function then prints the length of this list followed by its elements, separated by spaces, for each test case.

