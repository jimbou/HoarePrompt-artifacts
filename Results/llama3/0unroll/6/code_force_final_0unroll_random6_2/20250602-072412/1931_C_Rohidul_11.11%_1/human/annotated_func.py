#State of the program right berfore the function call: stdin contains multiple inputs: first an integer t, then t times: first an integer n, then n integers.
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
        
    #State: The output state will contain the maximum possible length of the subarray that can be obtained by removing the minimum number of elements from the given array, for each of the t test cases. The output will be in the format of t integers, each representing the maximum possible length of the subarray for the corresponding test case.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of an integer array. It calculates and prints the maximum possible length of a subarray that can be obtained by removing the minimum number of elements from the given array, for each test case. The function handles arrays with repeated elements at the start and end, as well as arrays with distinct start and end elements. It outputs the maximum possible subarray length for each test case, which can be zero if the array cannot be reduced to a single element.

