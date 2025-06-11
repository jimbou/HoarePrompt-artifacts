#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains three integers n, k, and x (1 ≤ n ≤ 2 * 10^5, 1 ≤ x, k ≤ n). The second line contains n integers a_1, a_2, …, a_n (1 ≤ a_i ≤ 1000). The number of test cases is given by an integer t (1 ≤ t ≤ 10^4) in the first line of stdin.
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
        
    #State: `t` is an integer greater than or equal to 0, `_` is `t-1`, `n` is an integer, `k` is an integer that must be greater than or equal to 0, `x` is an integer that must be greater than or equal to 0, `a` is a list of integers in descending order, `i` is `k`, `ans1` is the sum of the integers in `a` minus 2 times the sum of the integers in `a` plus the sum of the integers at indices less than `k` in `a` minus 2 times the sum of the integers at indices `i + x` less than `n` in `a`, `ans2` is the maximum of `ans1` and the sum of the integers in `a` minus 2 times the sum of the integers in `a`, `stdin` is empty, and the maximum of `ans1` and the sum of the integers in `a` minus 2 times the sum of the integers in `a` is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains three integers: the number of elements, a threshold value, and a penalty value. The second line contains a list of integers. For each test case, the function sorts the list of integers in descending order, calculates the maximum possible sum by applying a penalty to the first 'x' elements and then adding the next 'k' elements while avoiding the penalty, and prints the maximum sum. The function repeats this process for all test cases and then exits, leaving the standard input empty.

