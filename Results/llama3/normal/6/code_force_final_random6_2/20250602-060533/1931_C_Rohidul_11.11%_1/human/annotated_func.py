#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 <= n <= 2 * 10^5) and then a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= n).
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
        
    #State: n is greater than 0, a is a list of n integers where at least the last (n - k) elements are equal, l is k, r is l, st is k, end is n - k, _ is equal to the number of test cases in stdin, stdin contains no inputs. If the first element of a is equal to the last element of a, then ans is -1. If the first element of a is not equal to the last element of a, then if st is 0, end is 0, ans is n - 1, otherwise ans is 0, and the maximum value between 0 and ans is printed, which is 0 if ans is -1 or 0, and n - 1 if ans is n - 1

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a list of n integers. It then processes each test case by finding the longest contiguous subarray with distinct elements, excluding the first and last elements if they are equal. The function prints the maximum length of such a subarray for each test case, or 0 if no such subarray exists.

