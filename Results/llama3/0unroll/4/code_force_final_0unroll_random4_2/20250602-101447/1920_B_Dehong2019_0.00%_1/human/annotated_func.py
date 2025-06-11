#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains three integers t, k, and x (1 <= t <= 10^4, 1 <= k,x <= t). The second line contains t integers a_1, a_2,...,a_t (1 <= a_i <= 1000).
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
        
    #State: Output State: The loop has executed t times, and for each iteration, it has calculated the maximum possible sum of the array a after removing k elements and subtracting x from the sum. The output state is the same as the initial state, with the addition of t printed values, each representing the maximum possible sum for the corresponding test case. The value of t remains unchanged, and the contents of stdin have been consumed.

#Overall this is what the function does:This function reads multiple test cases from standard input, each containing three integers (t, k, x) and a list of t integers. It calculates the maximum possible sum of the list after removing k elements and subtracting x from the sum, and prints this value for each test case. The function consumes the contents of standard input and produces t output values, one for each test case.

