#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains three integers n, k, and x (1 ≤ n ≤ 2 * 10^5, 1 ≤ x, k ≤ n). The second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 1000).
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
            ans = max(ans1, ans2)
        
        print(ans)
        
    #State: `t` is an integer greater than or equal to 0, `_` is `t`, `n` is an integer, `k` is an integer greater than or equal to 0, `x` is an integer greater than or equal to 0, `a` is a list of integers in descending order, `ans1` is the sum of the integers in `a` minus twice the sum of the first `x` integers in `a` minus twice the sum of the first `x` integers in `a` plus the sum of the first `k` integers in `a`, `ans2` is the sum of the integers in `a` minus twice the sum of the first `x` integers in `a` minus twice the sum of the first `x` integers in `a`, `ans` is the maximum of `ans1` and `ans2`, `stdin` contains multiple test cases minus `t`, and `i` is `k-1`.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains three integers: the number of elements, a threshold value, and a penalty value. The second line contains a list of integers. The function then calculates the maximum possible sum of the integers in the list, considering the penalty value and the threshold value, and prints the result for each test case. The function processes all test cases and does not return any value.

