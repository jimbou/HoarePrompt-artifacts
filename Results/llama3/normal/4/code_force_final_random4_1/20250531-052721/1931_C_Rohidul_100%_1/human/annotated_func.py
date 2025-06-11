#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 2 * 10^5) followed by a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= n).
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
        
    #State: n is an integer greater than or equal to 1, a is a list of n integers, le is equal to n, l is equal to the index of the first element in a that is not equal to the first element in a, r is equal to the index of the last element in a that is equal to the last element in a, st is equal to the number of consecutive equal elements at the beginning of a, end is equal to the number of consecutive equal elements at the end of a. If the first element of a is equal to the last element of a, then ans is equal to max(0, le - (st + end)), otherwise ans is equal to le - max(st, end), and the value of ans is being printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a list of n integers. It then analyzes the list to find the number of consecutive equal elements at the beginning and end of the list, and calculates the minimum number of elements that need to be removed to make the list either empty or have no consecutive equal elements at the beginning and end. The function prints this minimum number for each test case.

