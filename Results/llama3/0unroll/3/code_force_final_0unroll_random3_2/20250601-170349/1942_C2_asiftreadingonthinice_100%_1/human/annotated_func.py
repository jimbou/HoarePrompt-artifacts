#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of two lines. The first line contains three integers n, x, and y (4 <= n <= 10^9, 2 <= x <= min(n, 2 * 10^5), 0 <= y <= n - x). The second line contains x distinct integers from 1 to n.
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
            elif (a[i] - a[i - 1]) % 2 == 0:
                tmp.append((a[i] - a[i - 1]) // 2)
        
        if a[0] + n - a[len(a) - 1] == 2:
            ans += 1
        elif (a[0] + n - a[len(a) - 1]) % 2 == 0:
            tmp.append((a[0] + n - a[len(a) - 1]) // 2)
        
        tmp.sort()
        
        for i in tmp:
            if y >= i - 1:
                ans += i
                y -= i - 1
            else:
                break
        
        ans += y
        
        print(min(ans, n - 2))
        
    #State: Output State: The output state after the loop executes all the iterations is a list of integers, where each integer represents the minimum number of operations required to make the array a permutation of the numbers from 1 to n, for each test case. The list has a length of t-1, where t is the initial value of tt. The output state is in the same format as the initial execution state, with the same variable names and data types. The values of the variables in the loop head and body have been updated after the loop executes all the iterations.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and outputs the minimum number of operations required to make an array a permutation of numbers from 1 to n for each test case. It accepts no parameters and returns a list of integers representing the minimum number of operations required for each test case. The function performs the following actions: reads input, sorts the array, calculates the minimum number of operations required, and outputs the result for each test case.

