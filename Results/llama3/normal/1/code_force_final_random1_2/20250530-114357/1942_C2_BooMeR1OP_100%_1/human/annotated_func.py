#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains three integers: n, x, and y, where n is the number of sides of the polygon, x is the number of vertices Bessie has chosen, and y is the maximum number of other vertices that can be chosen. The second line contains x distinct integers from 1 to n, representing the vertices Bessie has chosen. The constraints are 1 <= t <= 10^4, 4 <= n <= 10^9, 2 <= x <= min(n, 2 * 10^5), and 0 <= y <= n - x.
    t = int(input())
    for _ in range(t):
        n, x, y = list(map(int, input().split()))
        
        a = list(map(int, input().split()))
        
        a = [(num - 1) for num in a]
        
        ans = x - 2
        
        st = set(a)
        
        a.sort()
        
        for i in range(x):
            t1 = (a[i] + 1) % n
            t2 = (a[i] + 2) % n
            if t1 not in st and t2 in st:
                ans += 1
        
        odd = []
        
        even = []
        
        for i in range(x):
            next_elem = a[0] + n if i == x - 1 else a[i + 1]
            gap = next_elem - a[i] - 1
            if gap > 1 and gap % 2 == 1:
                odd.append(gap)
            elif gap > 0 and gap % 2 == 0:
                even.append(gap)
        
        odd.sort()
        
        even.sort()
        
        for gap in odd:
            if y < gap // 2:
                ans += 2 * y
                y = 0
                break
            ans += gap
            y -= gap // 2
        
        for gap in even:
            if y < gap // 2:
                ans += 2 * y
                y = 0
                break
            ans += gap
            y -= gap // 2
        
        print(ans)
        
    #State: ans is an integer equal to its original value plus the sum of all elements in the sorted list odd plus the sum of all elements in the even list, y is 0, i is x - 1, t1 is (a[x - 1] + 1) % n, t2 is (a[x - 1] + 2) % n, x is greater than or equal to 0, next_elem is a[0] + n, odd is an empty list, even is an empty list, n is an integer, a is a sorted list of integers, st is a set of integers, t is 0, stdin contains no input, and gap does not exist because even has been exhausted, and the value of ans which is the original value of ans plus the sum of all elements in the even list is being printed

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a polygon with n sides, x chosen vertices, and a maximum of y additional vertices that can be chosen. It calculates the maximum number of vertices that can be chosen, considering the constraints of the polygon and the chosen vertices. The function then prints the maximum number of vertices that can be chosen for each test case.

