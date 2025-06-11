#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains three integers t, k, and x (1 ≤ t ≤ 10^4, 1 ≤ k,x ≤ n). The second line contains n integers a_1, a_2, …, a_n (1 ≤ a_i ≤ 1000).
    for _ in range(int(input())):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        a.reverse()
        
        sum1 = sum(a)
        
        ans = []
        
        for i in range(k + 1):
            if i == 0:
                sums = sum1 - 2 * sum(a[:x])
                ans.append(sums)
            elif i + x - 1 < n:
                sums = sums + a[i - 1] - 2 * a[i + x - 1]
                ans.append(sums)
            else:
                sums = sums + a[i - 1]
                ans.append(sums)
        
        print(max(ans))
        
    #State: `n` is an integer, `x` is an integer, `a` is a list of integers in descending order, `sum1` is the sum of the integers in `a`, `_` is `t`, `t` is at least 0, `k` is at least 0, `i` is `k`, `ans` is a list containing the updated sums. If `i` is 0, `ans` is a list containing the value of `sum1 - 2 * sum(a[:x])`. If `i` is not 0, `ans` is a list containing the updated sums if `i + x - 1` is less than `n`, otherwise `ans` is a list containing the sum of the integers in `a` plus `a[i - 1]`, and the maximum value of the list `ans` is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains three integers: the number of elements, a threshold value, and a selection size. The second line contains a list of integers. The function sorts the list in descending order, calculates the sum of the integers, and then iterates over a range of values from 0 to the threshold value. For each iteration, it calculates an updated sum by subtracting twice the value of the selected integers or adding the previous integer if the selection size exceeds the list length. The function stores these updated sums in a list and finally prints the maximum value from this list. The function repeats this process for all test cases.

