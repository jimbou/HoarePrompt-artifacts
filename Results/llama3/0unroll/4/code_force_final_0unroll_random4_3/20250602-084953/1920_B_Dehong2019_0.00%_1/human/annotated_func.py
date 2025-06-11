#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains three integers t, n, and k (1 <= t <= 10^4, 1 <= n <= 2 * 10^5, 1 <= k <= n). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 1000).
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
        
    #State: Output State: The loop has executed t times, and for each execution, it has read two lines from the standard input. The first line contains three integers n, k, and x, and the second line contains n integers a_1, a_2, ..., a_n. The loop has calculated and printed the maximum possible sum of the array elements after applying the given operations. The values of t, n, k, x, and a_i have been used and modified within the loop, but their initial values are no longer accessible. The standard input has been consumed by the loop, and its state has been modified.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains three integers t, n, and k, and the second line contains n integers. The function calculates and prints the maximum possible sum of the array elements after applying certain operations, which involve sorting the array, subtracting twice the value of the first x elements, and then adding the value of the first k elements and subtracting twice the value of the elements at index k+x. The function repeats this process for each test case and prints the maximum sum for each case.

