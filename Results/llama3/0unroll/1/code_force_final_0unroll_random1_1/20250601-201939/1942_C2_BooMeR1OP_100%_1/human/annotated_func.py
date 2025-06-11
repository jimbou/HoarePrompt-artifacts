#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of two lines. The first line contains three integers n, x, and y (4 <= n <= 10^9, 2 <= x <= min(n, 2 * 10^5), 0 <= y <= n - x). The second line contains x distinct integers from 1 to n.
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
        
    #State: The loop will output the maximum number of integers that can be removed from the list a such that the remaining integers are in increasing order and the difference between any two adjacent integers is at most 2, for each of the t test cases. The output will be t integers, each on a new line.

#Overall this is what the function does:The function takes as input a series of test cases, where each test case consists of a list of integers and a target value. It then calculates and prints the maximum number of integers that can be removed from the list such that the remaining integers are in increasing order and the difference between any two adjacent integers is at most 2, for each test case.

