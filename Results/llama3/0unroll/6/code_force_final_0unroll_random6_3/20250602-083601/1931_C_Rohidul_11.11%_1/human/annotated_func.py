#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer and then a list of integers. The integer is a positive integer and represents the length of the list. The list contains positive integers. The sum of the lengths of all lists does not exceed 2 * 10^5.
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
        
    #State: The output state will contain the maximum possible length of the subarray that can be obtained by removing the first and last elements of the array, or the entire array if the first and last elements are the same. The output will be a list of integers, where each integer represents the maximum possible length for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a positive integer and a list of positive integers. It then processes each test case to find the maximum possible length of a subarray that can be obtained by removing the first and last elements of the array, or the entire array if the first and last elements are the same. The function prints the maximum possible length for each test case, which can be 0 or more.

