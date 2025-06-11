#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of two lines. The first line contains three integers n, x, and y (4 <= n <= 10^9, 2 <= x <= min(n, 2 * 10^5), 0 <= y <= n - x). The second line contains x distinct integers from 1 to n.
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    a = [(num - 1) for num in a]
    a.sort()
    present = set(a)
    ans = x - 2
    for i in range(x):
        t1 = (a[i] + 1) % n
        
        t2 = (a[i] + 2) % n
        
        if t1 not in present and t2 in present:
            ans += 1
        
    #State: n is an integer between 4 and 10^9, x is an integer equal to 0, y is an integer between 0 and n, a is a sorted list of 0 distinct integers from 0 to n-1, present is a set of 0 distinct integers from 0 to n-1, ans is an integer equal to 0, i is x, t1 is an integer equal to (a[i] + 1) % n, t2 is an integer equal to (a[i] + 2) % n, stdin contains t-1 test cases.
    gaps = []
    for i in range(x):
        next_elem = a[(i + 1) % x] + (n if i == x - 1 else 0)
        
        gap = next_elem - a[i] - 1
        
        if gap > 0:
            gaps.append(gap)
        
    #State: `n` is an integer between 4 and 10^9, `x` is an integer greater than or equal to 0, `y` is an integer between 0 and `n`, `a` is a sorted list of `n` distinct integers from 0 to `n-1`, `present` is a set of `n` distinct integers from 0 to `n-1`, `ans` is an integer equal to 0, `i` is equal to `x`, `t1` is an integer equal to (`a[x-1] + 1`) % `n`, `t2` is an integer equal to (`a[x-1] + 2`) % `n`, `gaps` is a list containing one or two integers, the first integer is equal to (`a[(x-1 + 1) % x] + (n if x-1 == x - 1 else 0)`) - `a[x-1] - 1`, and if the current value of `gap` is greater than 0, the second integer is equal to the current value of `gap`, `stdin` contains `t-1` test cases, `next_elem` is an integer equal to `a[(x-1 + 1) % x] + (n if x-1 == x - 1 else 0)`, and the current value of `gap` is an integer greater than or equal to 0. If `gap` is greater than 0, `gaps` contains two integers.
    gaps.sort()
    for gap in gaps:
        pairs = gap // 2
        
        if y >= pairs:
            ans += gap
            y -= pairs
        else:
            ans += 2 * y
            break
        
    #State: n is an integer between 4 and 10^9, x is an integer greater than or equal to 0, y is an integer between 0 and n, a is a sorted list of n distinct integers from 0 to n-1, present is a set of n distinct integers from 0 to n-1, i is equal to x, t1 is an integer equal to (a[x-1] + 1) % n, t2 is an integer equal to (a[x-1] + 2) % n, gaps is an empty list, stdin contains t-1 test cases, next_elem is an integer equal to a[(x-1 + 1) % x] + (n if x-1 == x - 1 else 0), ans is an integer equal to the sum of all integers in the list gaps plus 2 times the minimum of y and the sum of all pairs, and y is an integer equal to the maximum of 0 and y minus the sum of all pairs.
    print(ans)
    #This is printed: 0 + 2 * min(y, sum of all pairs) (where y is the maximum of 0 and y minus the sum of all pairs, and sum of all pairs is the sum of all pairs)

#Overall this is what the function does:This function calculates the maximum number of pairs that can be formed from a given set of integers, considering the gaps between consecutive integers and the availability of a certain number of pairs. It takes as input a set of integers and the number of pairs available, and returns the maximum number of pairs that can be formed. The function first sorts the input integers and calculates the gaps between consecutive integers. It then iterates over the gaps, calculating the number of pairs that can be formed from each gap and updating the total number of pairs accordingly. The function finally returns the total number of pairs that can be formed.

