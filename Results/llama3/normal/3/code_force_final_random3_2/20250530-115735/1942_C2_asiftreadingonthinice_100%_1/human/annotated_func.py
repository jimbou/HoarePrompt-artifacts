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
        
    #State: `tt` is at least `len(a)` + 1, `ii` is `tt` - 1, `n` is an integer, `x` is an integer, `a` is a sorted list of integers with at least two elements, `tmp` is a sorted list of integers with at least one element, `i` is the last element in the list `tmp`, `ans` is increased by the sum of all elements in `tmp` that are less than or equal to `y` + 1 plus `y`, and `y` is decreased by the sum of all elements in `tmp` that are less than or equal to `y` + 1 minus the number of elements in `tmp` that are less than or equal to `y` + 1, and the minimum of `ans` and `n - 2` is printed

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the minimum number of operations required to make a sequence of integers consecutive. It takes no arguments and returns no value. The function reads an integer t, representing the number of test cases, followed by t test cases. Each test case consists of three integers n, x, and y, and a list of x distinct integers from 1 to n. The function sorts the list of integers, calculates the number of operations required to make the sequence consecutive, and prints the minimum of this number and n-2. The function repeats this process for each test case.

