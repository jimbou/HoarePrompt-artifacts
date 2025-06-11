#State of the program right berfore the function call: stdin contains multiple inputs: first an integer t (1 <= t <= 10^4), then t times: first an integer n (1 <= n <= 2 * 10^5) and then n integers a_1, a_2, ..., a_n (1 <= a_i <= n).
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
        
    #State: t is 0, n is an integer between 1 and 2 * 10^5, a is a list of n integers between 1 and n, the longest prefix of a where all elements are equal is less than n - 1, the last two elements of a are equal, l is the length of the longest prefix of a where all elements are equal, r is equal to l, st is the length of the longest prefix of a where all elements are equal, end is equal to n - l - 1, stdin contains 0 inputs. If the first element of a is equal to the last element of a, then ans is equal to r - l - 1. If the first element of a is not equal to the last element of a, then if st is 0, end is 0, ans is equal to n - 1. Otherwise, ans is equal to r - l, and the maximum of 0 and ans is printed, which is either 0, r - l, or n - 1 depending on the values of st, end, and the first and last elements of a.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by n integers. It then calculates the length of the longest contiguous subarray with equal elements, excluding the first and last elements if they are equal. If the first and last elements are not equal, it returns the length of the longest contiguous subarray with equal elements, excluding the first element if it is not equal to the last element. The function prints the maximum of 0 and the calculated length for each test case.

