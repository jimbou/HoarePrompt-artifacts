#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains three integers n, k, and x (1 <= n <= 2 * 10^5, 1 <= x, k <= n). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 1000). The number of test cases is specified by a single integer t (1 <= t <= 10^4) in the first line of the input.
    """
    Created on Fri Sep  6 21:42:15 2024
     
    @author: dehon
    """
    t = int(input())
    for _ in range(t):
        n, k, x = map(int, input().split())
        
        a = sorted(list(map(int, input().split())), reverse=True)
        
        ans1 = sum(a)
        
        for i in range(x):
            ans1 -= a[i] * 2
        
        ans2 = ans1
        
        for i in range(k):
            ans1 += a[i]
            if i + x < n:
                ans1 -= a[i + x] * 2
            ans2 = max(ans1, ans2)
        
        print(ans2)
        
    #State: `t` is an integer greater than or equal to 0, `_` is `t`, `n` is an integer, `k` is an integer, `x` is an integer, `a` is a sorted list of integers in descending order, `i` is `k-1`, `ans1` is the sum of the integers in `a` minus 2 times the sum of the integers in `a` from index 0 to `x-1` plus the sum of the integers in `a` from index 0 to `k-1` minus 2 times the sum of the integers in `a` from index `x` to `k+x-1`, `ans2` is the maximum of `ans1` and the sum of the integers in `a` minus 2 times the sum of the integers in `a` from index 0 to `x-1` and the maximum of the previous `ans1` and the sum of the integers in `a` minus 2 times the sum of the integers in `a` from index 0 to `x-1`, and the maximum of `ans1` and the previous value of `ans2` has been printed for `t` times, and `stdin` is empty.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains three integers n, k, and x, and the second line contains n integers. The function processes each test case by sorting the integers in descending order, calculating the sum of the integers minus 2 times the sum of the first x integers, and then iteratively adding and subtracting integers from the sum while keeping track of the maximum sum. The function prints the maximum sum for each test case.

