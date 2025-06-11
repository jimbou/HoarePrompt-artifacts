#State of the program right berfore the function call: stdin contains two inputs: first an integer (t) and then t pairs of integers (n, k) where 1 <= t <= 1000, 2 <= n <= 10^6, 1 <= k <= n.
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
        
    #State: `t` is 0, `tc` is `t` + 1, `n` is an integer between 2 and 10^6 (inclusive), `k` is an integer between 1 and `n` (inclusive), `i` is the smallest integer greater than or equal to log2(`k`), `ans` is a list containing 23 integers: `k - (1 << i)`, `k + 1`, `k + 1 + (1 << i)`, and 20 integers of the form 1 << j for j in range(20) where j is not equal to i, stdin is empty, and `j` is 20.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two integers: n and k. For each test case, it generates a list of 23 integers based on the value of k and prints the length of the list followed by the list itself. The list contains three specific integers related to k and twenty integers that are powers of 2, excluding the power of 2 that is closest to k. The function processes all test cases and then terminates, leaving the standard input empty.

