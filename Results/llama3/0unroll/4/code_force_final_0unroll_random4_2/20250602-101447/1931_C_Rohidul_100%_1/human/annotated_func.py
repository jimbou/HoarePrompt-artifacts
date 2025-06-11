#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (1 <= n <= 2 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= n).
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        le = len(a)
        
        l, r = 0, n - 1
        
        st, end = 1, 1
        
        while l < r and a[l] == a[l + 1]:
            l += 1
            st += 1
        
        while r > l and a[r] == a[r - 1]:
            r -= 1
            end += 1
        
        ans = le - max(st, end)
        
        if a[0] == a[-1]:
            ans = max(0, le - (st + end))
        
        print(ans)
        
    #State: The output state will contain the same number of test cases as the initial state. Each test case will contain a single integer, which represents the minimum number of elements that need to be removed from the array to make all elements equal. The output state will be in the same format as the initial state, with each test case on a new line.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a list of integers. It then determines the minimum number of elements that need to be removed from the list to make all elements equal. The function considers two cases: when the first and last elements are equal, and when they are not. It calculates the minimum number of removals required in each case and prints the result for each test case.

