#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains three integers: n, x, and y (4 <= n <= 10^9, 2 <= x <= min(n, 2 * 10^5), 0 <= y <= n - x). The second line contains x distinct integers from 1 to n.
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
        
    #State: tt is greater than or equal to 0, ii is equal to tt, n is an integer, x is an integer, a is a sorted list of integers, tmp is a sorted list containing the integer values of half of the even differences between consecutive elements in a, including the half of the difference between the first element of a and the last element of a plus n, if the difference between the first element of a and the last element of a plus n is even, otherwise tmp remains unchanged, ans is increased by 1 if the difference between the first element of a, n, and the last element of a is 2, and ans is increased by the number of pairs of consecutive elements in a with a difference of 2, plus the sum of all elements in tmp minus the length of tmp plus 1, i is equal to the last element in tmp, y is 0, and the minimum value between ans and n - 2 is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains three integers: n, x, and y, and the second line contains x distinct integers from 1 to n. The function sorts the integers, calculates the number of pairs of consecutive integers with a difference of 2, and calculates the sum of half of the even differences between consecutive integers, including the half of the difference between the first integer, n, and the last integer, if the difference is even. The function then prints the minimum value between the calculated sum and n-2 for each test case.

