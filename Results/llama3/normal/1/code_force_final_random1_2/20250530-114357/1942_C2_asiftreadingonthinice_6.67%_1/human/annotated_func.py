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
        
    #State: tt is greater than or equal to 0, ii is equal to tt, n is an integer, x is an integer, y is an integer, a is a sorted list of integers, stdin is empty, i is equal to the length of a, ans is x + y - 2 plus the sum of all the differences between consecutive elements in a that are equal to 2, plus the sum of half of the differences between consecutive elements in a that are even and for which y is greater than half of the difference minus 1, plus y. If the difference between the first element of a, n and the last element of a is equal to 2, then ans is increased by 1. If the difference between the first element of a, n and the last element of a is even and y is greater than half of this difference minus 1, then y is decreased by half of this difference minus 1, ans is increased by half of this difference, and tmp is appended with half of this difference. Otherwise, the values of y, ans, and tmp remain unchanged, and the minimum value between ans and n-2 is printed.

#Overall this is what the function does:Functionality: This function reads a series of test cases from standard input, where each test case consists of three integers (n, x, y) and a list of x distinct integers from 1 to n. It then calculates the minimum number of operations required to make all numbers in the list consecutive, considering the availability of y "moves" to fill gaps. The function prints the minimum number of operations required for each test case, which is the minimum value between the calculated answer and n-2.

