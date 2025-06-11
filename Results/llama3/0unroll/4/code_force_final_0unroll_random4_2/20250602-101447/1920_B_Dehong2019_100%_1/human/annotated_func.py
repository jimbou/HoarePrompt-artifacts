#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains three integers n, k, and x (1 <= n <= 2 * 10^5, 1 <= x, k <= n). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 1000). The number of test cases is specified by a single integer t (1 <= t <= 10^4) in the first line of stdin.
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
        
    #State: The output state is the maximum possible sum of the array elements after applying the given operations for each test case. The operations involve subtracting twice the value of the first x elements and then adding the value of the first k elements and subtracting twice the value of the elements at index k+x, if it exists. The maximum sum is calculated and printed for each test case. The input state remains unchanged, with t test cases still in stdin, each consisting of two lines with the same format as the initial state.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines: the first line contains three integers (n, k, and x) and the second line contains n integers. It then calculates the maximum possible sum of the array elements after applying specific operations (subtracting twice the value of the first x elements, adding the value of the first k elements, and subtracting twice the value of elements at index k+x if it exists) and prints this maximum sum for each test case. The input state remains unchanged.

