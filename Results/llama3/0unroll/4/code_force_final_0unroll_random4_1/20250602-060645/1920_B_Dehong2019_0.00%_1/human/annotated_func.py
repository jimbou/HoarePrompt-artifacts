#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains three integers t, k, and x (1 ≤ t ≤ 10^4, 1 ≤ k, x ≤ n). The second line contains n integers a_1, a_2, …, a_n (1 ≤ a_i ≤ 1000).
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
        
    #State: The loop has executed t times, and for each execution, it has printed the maximum value of ans1 and ans2. The values of n, k, x, and a have been updated for each test case, but their initial values are not retained. The final output state is the last printed value of ans, which is the maximum value of ans1 and ans2 for the last test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains three integers t, k, and x, and the second line contains n integers. For each test case, it calculates the maximum value of a modified sum of the integers, considering the values of k and x, and prints this maximum value. The function repeats this process for all test cases and does not retain any information from previous test cases.

