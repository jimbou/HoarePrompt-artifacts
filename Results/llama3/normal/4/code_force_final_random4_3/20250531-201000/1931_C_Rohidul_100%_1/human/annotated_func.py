#State of the program right berfore the function call: stdin contains multiple inputs: first an integer t, then for each test case, first an integer n, then a space-separated list of n integers. The integers are non-negative and less than or equal to n.
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
        
    #State: t is an integer greater than or equal to 0, n is an integer, a is a list of n non-negative integers less than or equal to n, le is n, l is less than or equal to r, r is greater than or equal to l, st is the number of elements in a that are equal to the first element of a, end is the number of elements in a that are equal to the last element of a, ans is n - max(st, end) if the first element of a is not equal to the last element of a. Otherwise, ans is max(0, le - (st + end)), and ans is printed, and stdin contains no input.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by a list of n non-negative integers. It then calculates the minimum number of elements that need to be removed from the list so that the remaining elements are either all equal to the first element or all equal to the last element. If the first and last elements are the same, it calculates the maximum number of elements that can be removed while still satisfying the condition. The function prints the result for each test case.

