#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains three integers n, k, and x (1 <= n <= 2 * 10^5, 1 <= x, k <= n). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 1000).
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
        
    #State: The output state will be the maximum sum of the array elements after removing 2*x elements from the array, where x is the number of elements to be removed in each iteration, and the array is sorted in descending order. The maximum sum is calculated for each iteration of the loop, and the final output is the maximum sum among all iterations.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of two lines. The first line contains three integers: n (the number of elements), k, and x (the number of elements to remove in each iteration). The second line contains n integers representing the array elements. The function sorts the array in descending order, then iterates k+1 times, calculating the sum of the remaining elements after removing 2*x elements in each iteration. The function outputs the maximum sum obtained among all iterations for each test case.

