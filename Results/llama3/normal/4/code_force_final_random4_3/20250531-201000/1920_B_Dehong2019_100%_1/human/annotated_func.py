#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains three integers n, k, and x (1 <= n <= 2 * 10^5, 1 <= x, k <= n). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 1000).
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
        
    #State: t is an integer equal to 0, n is an integer, k is an integer greater than or equal to 0, a is a list of integers sorted in descending order, ans1 is the sum of the integers in list a minus twice the sum of the integers in list a from index 0 to x-1 plus the sum of the integers in list a from index 0 to k-1 minus twice the sum of the integers in list a from index x to k+x-1, ans2 is the maximum of ans1 and its previous value, i is equal to k, stdin contains no inputs, and x is an integer, and ans2 is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains three integers n, k, and x, and the second line contains n integers. The function then calculates the maximum possible sum of the integers in each test case by applying certain operations, and prints the maximum sum for each test case. The operations involve sorting the integers in descending order, subtracting twice the sum of the first x integers, adding the sum of the first k integers, and subtracting twice the sum of the integers from index x to k+x-1. The function repeats this process for each test case and prints the maximum sum obtained for each case.

