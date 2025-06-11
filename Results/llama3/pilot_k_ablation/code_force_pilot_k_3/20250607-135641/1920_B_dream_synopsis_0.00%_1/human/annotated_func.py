#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains three space-separated integers: n, k, and x (1 <= n <= 2 * 10^5, 1 <= x, k <= n). The second line contains n space-separated integers a_1, a_2, ..., a_n (1 <= a_i <= 1000).
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
        
    #State: n is an integer, k is an integer that must be greater than or equal to 0, x is an integer, a is a sorted list of integers in descending order, sum1 is the sum of the integers in a, stdin is empty, _ is increased by k + 1, the number of iterations is increased by k + 1. ans is a list containing the value of sums. If i is 0, sums is equal to sum1 - 2 * sum(a[:x + 1]). If i is not 0, if i + x - 1 is less than n, sums is increased by a[i - 1] - 2 * a[i + x - 1]. Otherwise, sums is increased by a[i - 1]., and the maximum value from the list ans is printed, which is the maximum calculated sum of the integers in the list a after the specified operations.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains three integers: n, k, and x. The second line contains n integers. The function sorts these integers in descending order, calculates a series of sums by subtracting twice the sum of the first x+1 integers and then iteratively adding or subtracting integers based on their position and the value of x, and finally prints the maximum sum calculated. The function repeats this process for each test case until standard input is empty.

