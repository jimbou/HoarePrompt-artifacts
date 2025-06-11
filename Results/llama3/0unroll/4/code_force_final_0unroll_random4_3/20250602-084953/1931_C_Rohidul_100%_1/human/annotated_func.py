#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer and then a list of integers. The integer is a positive integer and represents the length of the list. The list contains positive integers. The number of test cases is a positive integer (1 ≤ t ≤ 10^4) and the sum of the lengths of the lists for all test cases does not exceed 2⋅10^5.
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
        
    #State: The output state after the loop executes all the iterations is a list of integers, where each integer represents the minimum number of elements that need to be removed from the corresponding list in the input to make it a list with alternating elements.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of a positive integer representing the length of a list and the list itself containing positive integers. It calculates and prints the minimum number of elements that need to be removed from each list to make it a list with alternating elements. If the first and last elements of the list are the same, it considers removing elements from both the start and end of the list to achieve the alternating pattern. The function outputs a list of integers, where each integer corresponds to the minimum number of removals required for each input list.

