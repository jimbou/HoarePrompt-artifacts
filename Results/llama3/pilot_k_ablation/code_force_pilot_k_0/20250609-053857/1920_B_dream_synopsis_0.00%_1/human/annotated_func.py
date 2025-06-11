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
                sums = sum1 - 2 * sum(a[:x + 1])
                ans.append(sums)
            elif i + x - 1 < n:
                sums = sums + a[i - 1] - 2 * a[i + x - 1]
                ans.append(sums)
            else:
                sums = sums + a[i - 1]
                ans.append(sums)
        
        print(max(ans))
        
    #State: The maximum sum of the array elements after removing k elements, where the removed elements are chosen to maximize the sum, for each test case.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of two lines. The first line contains three integers: the number of elements (n), the number of elements to remove (k), and a parameter (x). The second line contains n integers representing the elements of an array. The function sorts the array in descending order, calculates the sum of the array elements, and then iteratively calculates the maximum sum that can be obtained by removing k elements, considering the parameter x. For each test case, it prints the maximum sum that can be achieved.

