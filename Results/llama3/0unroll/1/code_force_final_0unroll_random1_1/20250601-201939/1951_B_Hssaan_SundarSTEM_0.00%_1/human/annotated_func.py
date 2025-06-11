#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines of input. The first line contains two space-separated integers: n and k (2 <= n <= 10^5, 1 <= k <= n). The second line contains n space-separated integers: a_1, a_2, ..., a_n (1 <= a_i <= 10^9) such that all a_i are distinct.
    for _ in range(int(input())):
        n, k = list(map(int, input().split()))
        
        s = list(map(int, input().split()))
        
        s[0], s[k - 1] = s[k - 1], s[0]
        
        ans = 0
        
        h = s[0]
        
        j = -1
        
        for i in s[1:]:
            j += 1
            if h < i:
                break
            else:
                ans += 1
        
        p = j
        
        s[0], s[k - 1] = s[k - 1], s[0]
        
        ans1 = 0
        
        s[p], s[k - 1] = s[k - 1], s[p]
        
        z = 0
        
        for i in s:
            if i == h:
                if s[0] != h:
                    ans1 += 1
                z = 1
            elif i > h:
                break
            elif z == 1:
                ans1 += 1
        
        print(max(ans, ans1))
        
    #State: The output state will be a series of integers, each representing the maximum number of elements that can be removed from the input list while maintaining the condition that the first element is greater than or equal to the last element. The number of integers in the output state will be equal to the number of test cases in the input state.

#Overall this is what the function does:The function reads multiple test cases from standard input, each containing a list of distinct integers and a target position. It swaps the first element with the element at the target position, then calculates the maximum number of elements that can be removed while maintaining the condition that the first element is greater than or equal to the last element. The function performs this calculation twice, once with the original list and once with the list modified by swapping the element at the target position with the element at the position of the first occurrence of the original first element. The function prints the maximum of these two calculations for each test case.

