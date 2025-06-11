#State of the program right berfore the function call: stdin contains multiple inputs: first an integer t (1 <= t <= 10^4), then for each test case, first an integer n (1 <= n <= 2 * 10^5) and then n integers a_1, a_2, ..., a_n (1 <= a_i <= n).
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
        
    #State: `_` is equal to `t`, stdin is empty, input() is equal to 0, and the maximum length of the subarray that can be obtained by removing at most one element from the list `a` such that the remaining elements are equal is printed for each test case.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the maximum length of the subarray that can be obtained by removing at most one element from the list `a` such that the remaining elements are equal for each test case. It accepts no parameters and returns no value, instead printing the results directly. The function consumes all input from stdin and leaves it empty.

