#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains three integers n, k, and x (1 ≤ n ≤ 2 * 10^5, 1 ≤ x, k ≤ n). The second line contains n integers a_1, a_2, …, a_n (1 ≤ a_i ≤ 1000). The number of test cases is specified by an integer t (1 ≤ t ≤ 10^4) on the first line of the input.
    for _ in range(int(input())):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        a.reverse()
        
        sum1 = sum(a)
        
        ans = []
        
        for i in range(k + 1):
            if i == 0:
                sums = sum1 - 2 * sum(a[:x])
                ans.append(sums)
            elif i + x - 1 < n:
                sums = sums + a[i - 1] - 2 * a[i + x - 1]
                ans.append(sums)
            else:
                sums = sums + a[i - 1]
                ans.append(sums)
        
        print(max(ans))
        
    #State: The maximum sum of the array elements after removing k elements, where the sum is calculated by subtracting twice the sum of the x largest elements from the total sum, and then iteratively adding the next largest element and subtracting twice the next largest element that is x positions ahead, until k elements have been removed.

#Overall this is what the function does:This function processes multiple test cases from standard input, each consisting of two lines. It reads three integers (n, k, and x) and an array of n integers, sorts the array in descending order, and calculates the maximum sum of the array elements after removing k elements. The sum is calculated by subtracting twice the sum of the x largest elements from the total sum, and then iteratively adding the next largest element and subtracting twice the next largest element that is x positions ahead, until k elements have been removed. The function prints the maximum sum for each test case.

