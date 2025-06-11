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
        
    #State: n is an integer greater than 1, a is a list of n integers between 1 and n, l is equal to r, r is greater than or equal to 0, st is r, end is equal to r + 1, stdin is empty. If the first and last elements of a are equal, then ans is equal to r - l - 1. If the first and last elements of a are not equal, then if st is 0 and end is 0, ans is n-1; otherwise, ans is 0. The maximum of 0 and ans is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a list of n integers. It then processes each test case to find the maximum possible length of a subarray that can be obtained by removing a prefix and/or suffix of equal elements. If the first and last elements of the list are equal, it calculates the length of the subarray by subtracting 1 from the difference between the right and left pointers. If the first and last elements are not equal, it checks if the list has no repeated elements at the start and end, and if so, it returns the length of the list minus 1. Otherwise, it returns 0. The function prints the maximum of 0 and the calculated length for each test case.

