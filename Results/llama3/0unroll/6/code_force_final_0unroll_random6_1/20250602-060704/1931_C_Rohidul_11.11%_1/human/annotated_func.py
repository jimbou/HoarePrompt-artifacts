#State of the program right berfore the function call: stdin contains multiple inputs: first an integer t (1 <= t <= 10^4), then for each test case, first an integer n (1 <= n <= 2 * 10^5) and then n integers a_1, a_2, ..., a_n (1 <= a_i <= n).
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        l, r = 0, n - 1
        
        st, end = 0, 0
        
        while l < r and a[l] == a[l + 1]:
            l += 1
            st += 1
        
        while r > l and a[r] == a[r - 1]:
            r -= 1
            end += 1
        
        if a[0] == a[-1]:
            ans = r - l - 1
        elif st == 0 and end == 0 and a[0] != a[-1]:
            ans = len(a) - 1
        else:
            ans = r - l
        
        print(max(0, ans))
        
    #State: The output state will be the maximum possible length of the subarray that can be obtained by removing the minimum number of elements from the input array, such that the remaining elements are either all equal or all different. The output will be a list of integers, where each integer represents the maximum possible length of the subarray for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by n integers. It then calculates and prints the maximum possible length of the subarray that can be obtained by removing the minimum number of elements from the input array, such that the remaining elements are either all equal or all different. The function handles three cases: when the first and last elements are equal, when the first and last elements are different and no elements need to be removed, and when elements need to be removed from the start or end of the array. The function returns a list of integers, where each integer represents the maximum possible length of the subarray for each test case.

