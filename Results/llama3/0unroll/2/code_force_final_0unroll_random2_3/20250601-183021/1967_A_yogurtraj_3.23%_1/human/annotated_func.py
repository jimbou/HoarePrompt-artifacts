#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains two integers n and k (1 <= n <= 2 * 10^5, 0 <= k <= 10^12). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^12).
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
            print((r - 1) * n + 1)
        else:
            print((r - 1) * n + 1 + rem + y)
        
    #State: The output state is a list of integers, where each integer represents the number of elements in the sorted array that are less than or equal to the corresponding element in the original array, plus the remainder of the division of the difference between the corresponding element in the original array and the smallest element in the sorted array by the number of elements in the sorted array, plus the number of elements in the sorted array that are greater than the corresponding element in the original array.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines: the first line contains two integers n and k, and the second line contains n integers. The function sorts the integers, then iterates through the sorted list to find the maximum value that can be achieved by subtracting a certain amount from each integer, based on the value of k. If k is not exhausted after iterating through the entire list, it calculates the maximum value that can be achieved by adding the remaining k to the last integer in the list. The function then prints the number of elements in the sorted list that are less than or equal to the calculated maximum value, plus the remainder of the division of the difference between the calculated maximum value and the smallest element in the sorted list by the number of elements in the sorted list, plus the number of elements in the sorted list that are greater than the calculated maximum value.

