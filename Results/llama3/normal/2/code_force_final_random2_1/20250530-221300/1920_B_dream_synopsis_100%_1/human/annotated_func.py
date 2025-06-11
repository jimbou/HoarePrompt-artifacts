#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains three integers n, k, and x (1 ≤ n ≤ 2 * 10^5, 1 ≤ x, k ≤ n). The second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 1000).
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
        
    #State: `n` is an integer, `k` is at least `k`, `x` is an integer, `a` is a list of integers in descending order, `sum1` is the sum of all integers in `a`, `stdin` is empty, `i` is `k`, and `ans` is a list containing the sums of the first `k` elements of `a`, and the maximum sum of the first `k` elements of `a` is being printed

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains three integers: the number of elements (n), a threshold (k), and a multiplier (x). The second line contains n integers. The function sorts these integers in descending order, calculates the sum of all integers, and then iterates k+1 times to calculate a series of sums by subtracting twice the value of the xth element and adding the previous element's value. It keeps track of these sums in a list and finally prints the maximum sum found. The function repeats this process for all test cases until standard input is empty.

