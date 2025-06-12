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
        
    #State: stdin contains 0 test cases, n is an integer, k is an integer, x is an integer, a is a list of integers in descending order, sum1 is the sum of the integers in a, ans is a list of integers where each integer is the sum of the integers in a minus twice the sum of the integers from index x+1 to i+x-1 (if i+x-1 is less than n) or the sum of the integers in a plus a[i-1] (if i+x-1 is not less than n), and the maximum value in the list ans has been printed for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains three integers n, k, and x, and the second line contains n integers. The function sorts the integers in descending order, calculates a series of sums by subtracting twice the sum of certain subsets of integers from the total sum, and prints the maximum of these sums for each test case. The function repeats this process until all test cases have been read from standard input.

