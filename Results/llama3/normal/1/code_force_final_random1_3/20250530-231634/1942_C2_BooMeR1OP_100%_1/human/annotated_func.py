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
        
    #State: t is an integer between 1 and 10^4, n is an integer, x is an integer, a is a sorted list of integers where each integer is one less than its original value, i is x, t1 is an integer equal to (a[x - 1] + 1) % n, t2 is an integer equal to (a[x - 1] + 2) % n, ans is an integer equal to x - 2 plus the number of times t1 is not in st and t2 is in st for all i from 0 to x - 1 plus the sum of all odd gaps between consecutive elements in a plus the sum of all even gaps between consecutive elements in a, odd is an empty list, even is an empty list, y is 0, gap is 0, _ is t - 1, t is 0, st is a set containing all elements of a, next_elem is an integer equal to a[0] + n, and ans is printed

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the result. It accepts an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of two lines: the first line contains three integers n, x, and y (4 <= n <= 10^9, 2 <= x <= min(n, 2 * 10^5), 0 <= y <= n - x), and the second line contains x distinct integers from 1 to n. The function processes each test case, calculates a result based on the input, and prints the result. The result is calculated by considering the gaps between consecutive elements in the sorted list of integers and adding up the odd and even gaps. The function also considers the number of times a certain condition is met and adds it to the result. Finally, the function prints the calculated result for each test case.

