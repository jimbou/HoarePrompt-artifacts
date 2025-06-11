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
        
    #State: `tt` is an integer between 1 and 10^4, `ii` is `tt - 1`, `n`, `x`, `y` are integers, `a` is a sorted list of integers, `i` is equal to the length of `a`, `ans` is an integer equal to `x + y - 2` plus the number of pairs of adjacent elements in `a` with a difference of 2 plus the sum of half of the differences of pairs of adjacent elements in `a` with an even difference and `y` greater than half of the difference minus 1 plus `y` plus 1 if the first element of `a` plus `n` minus the last element of `a` equals 2, otherwise `ans` is an integer equal to `x + y - 2` plus the number of pairs of adjacent elements in `a` with a difference of 2 plus the sum of half of the differences of pairs of adjacent elements in `a` with an even difference and `y` greater than half of the difference minus 1 plus half of the difference between the first element of `a`, `n` and the last element of `a` if the difference between the first element of `a`, `n` and the last element of `a` is even and `y` is greater than half of the difference between the first element of `a`, `n` and the last element of `a` minus 1, `tmp` is a list containing half of the differences of pairs of adjacent elements in `a` with an even difference and `y` greater than half of the difference minus 1 plus half of the difference between the first element of `a`, `n` and the last element of `a` if the difference between the first element of `a`, `n` and the last element of `a` is even and `y` is greater than half of the difference between the first element of `a`, `n` and the last element of `a` minus 1, and the minimum value between `ans` and `n - 2` is being printed, and `stdin` is empty.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the minimum value between the calculated answer and n-2. The input consists of an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of two lines. The first line contains three integers n, x, and y (4 <= n <= 10^9, 2 <= x <= min(n, 2 * 10^5), 0 <= y <= n - x). The second line contains x distinct integers from 1 to n. The function sorts the integers, calculates the answer based on the differences between adjacent elements, and prints the minimum value between the answer and n-2.

