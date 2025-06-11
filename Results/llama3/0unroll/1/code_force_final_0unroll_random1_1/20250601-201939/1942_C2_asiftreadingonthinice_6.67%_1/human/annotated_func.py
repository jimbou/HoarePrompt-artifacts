#State of the program right berfore the function call: stdin contains an integer t, followed by t test cases. Each test case consists of two lines. The first line contains three integers n, x, and y. The second line contains x distinct integers from 1 to n. The input satisfies the following constraints: 1 <= t <= 10^4, 4 <= n <= 10^9, 2 <= x <= min(n, 2 * 10^5), 0 <= y <= n - x.
    tt = int(input())
    for ii in range(tt):
        n, x, y = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        ans = x + y - 2
        
        tmp = []
        
        for i in range(1, len(a)):
            if a[i] - a[i - 1] == 2:
                ans += 1
            elif (a[i] - a[i - 1]) % 2 == 0 and y > (a[i] - a[i - 1]) // 2 - 1:
                tmp.append((a[i] - a[i - 1]) // 2)
                ans += (a[i] - a[i - 1]) // 2
                y -= (a[i] - a[i - 1]) // 2 - 1
        
        if a[0] + n - a[len(a) - 1] == 2:
            ans += 1
        elif (a[0] + n - a[len(a) - 1]) % 2 == 0 and y > (a[i] - a[i - 1]) // 2 - 1:
            tmp.append((a[0] + n - a[len(a) - 1]) // 2)
            ans += (a[i] - a[i - 1]) // 2
            y -= (a[i] - a[i - 1]) // 2 - 1
        
        ans += y
        
        print(min(ans, n - 2))
        
    #State: The output state after the loop executes all the iterations is a list of integers, where each integer is the minimum of the calculated answer and n-2 for each test case. The list contains t-1 integers, where t is the initial value of tt. The values of n, x, y, and a are updated for each test case, but their initial values are not affected by the loop.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers (n, x, y) and a list of x distinct integers from 1 to n. It calculates the minimum number of integers that can be added to the list to make it a contiguous sequence of integers from 1 to n, considering the constraints x, y, and the given list. The function then prints the minimum of the calculated answer and n-2 for each test case.

