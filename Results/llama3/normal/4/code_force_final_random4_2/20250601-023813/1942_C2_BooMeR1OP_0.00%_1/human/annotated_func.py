#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two lines. The first line contains three integers n, x, and y (4 <= n <= 10^9, 2 <= x <= min(n, 2 * 10^5), 0 <= y <= n - x). The second line contains x distinct integers from 1 to n.
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
        
    #State: n is an integer between 4 and 10^9, x is an integer between 2 and min(n, 2 * 10^5), y is an integer between 0 and n - x, a is a sorted list of x distinct integers from 0 to n - 1, present is a set of x distinct integers from 0 to n - 1, i is x - 1, t1 is an integer between 1 and n - 1, t2 is an integer between 2 and n - 1, ans is an integer equal to x - 1 + (x - 2) if t1 is not in the set present and t2 is in the set present, otherwise ans is an integer equal to x - 2 + (x - 2), stdin contains t - 1 test cases.
    gaps = []
    for i in range(x):
        next_elem = a[(i + 1) % x] + (n if i == x - 1 else 0)
        
        gap = next_elem - a[i] - 1
        
        if gap > 0:
            gaps.append(gap)
        
    #State: `n` is an integer between 4 and 10^9, `x` is an integer greater than 0, `y` is an integer between 0 and `n - x`, `a` is a sorted list of `x` distinct integers from 0 to `n - 1`, `present` is a set of `x` distinct integers from 0 to `n - 1`, `i` is `x - 1`, `t1` is an integer between 1 and `n - 1`, `t2` is an integer between 2 and `n - 1`, `ans` is an integer equal to `x - 1 + (x - 2)` if `t1` is not in the set `present` and `t2` is in the set `present`, otherwise `ans` is an integer equal to `x - 2 + (x - 2)`, `gaps` is a list containing `x` integers, each integer is equal to `next_elem - a[i] - 1`, and `stdin` contains `t - 1` test cases.
    gaps.sort()
    for gap in gaps:
        pairs = gap // 2
        
        if y >= pairs:
            ans += gap
            y -= pairs
        else:
            ans += 2 * y
            break
        
    #State: n is an integer between 4 and 10^9, x is an integer greater than 0, y is an integer between 0 and n - x, a is a sorted list of x distinct integers from 0 to n - 1, present is a set of x distinct integers from 0 to n - 1, i is x - 1, t1 is an integer between 1 and n - 1, t2 is an integer between 2 and n - 1, gaps is an empty list, stdin contains t - 1 test cases if y is greater than or equal to pairs, otherwise stdin contains t - (number of iterations) test cases. If y is greater than or equal to pairs, then ans is an integer equal to its original value plus the sum of all gaps, y is an integer equal to its original value minus the sum of all pairs. Otherwise, ans is an integer equal to its original value plus 2 * y, and stdin contains t - (number of iterations) test cases.
    print(ans)
    #This is printed: ans (where ans is the updated value of ans after the conditional update, which is either ans + sum of all gaps if y >= pairs, or ans + 2 * y otherwise)

#Overall this is what the function does:This function calculates the maximum number of pairs that can be formed from a given set of integers, considering the constraints of the problem. It takes as input the number of test cases, the number of integers in each test case, and the integers themselves. It then calculates the maximum number of pairs that can be formed by considering the gaps between the integers and the remaining available pairs. The function prints the maximum number of pairs that can be formed for each test case.

