#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains two integers n and k (1 <= n <= 2 * 10^5, 0 <= k <= 10^12). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^12).
    for ii in range(int(input())):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        r = a[0]
        
        rem = 0
        
        y = 0
        
        for i in range(0, n - 1):
            if (i + 1) * (a[i + 1] - a[i]) > k:
                r = a[i] + k // (i + 1)
                rem = k % (i + 1)
                y = n - 1 - i
                k = 0
                break
            else:
                k -= (i + 1) * (a[i + 1] - a[i])
                r = a[i + 1]
        
        if k != 0:
            r = a[n - 1] + k // n
            print((r - 1) * n + 1 + k % n)
        else:
            print((r - 1) * n + 1 + rem + y)
        
    #State: The output state after the loop executes all the iterations is a series of integers, each representing the number of elements in the sorted array that are less than or equal to the given value k. The value of k is updated after each iteration based on the difference between the current element and the previous element in the sorted array, and the number of elements remaining in the array. The final output state is a series of integers representing the number of elements in the sorted array that are less than or equal to the updated value of k.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines: the first line contains two integers n and k, and the second line contains n integers. The function sorts the integers, then iterates through the sorted list to find the number of elements less than or equal to a given value k, updating k based on the differences between consecutive elements and the remaining elements in the list. The function prints the number of elements less than or equal to the updated value of k for each test case.

