#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains three integers: n, x, and y (4 <= n <= 10^9, 2 <= x <= min(n, 2 * 10^5), 0 <= y <= n - x). The second line contains x distinct integers from 1 to n.
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
        
    #State: n is an integer between 4 and 10^9, x is an integer between 2 and min(n, 2 * 10^5), y is an integer between 0 and n - x, a is a sorted list of x distinct integers between 0 and n-1, present is a set containing the unique elements of a, stdin is empty, i is x, t1 is an integer equal to (a[x-1] + 1) % n, t2 is an integer equal to (a[x-1] + 2) % n, ans is an integer equal to x - 2 + k, where k is the number of times t1 is not in present and t2 is in present for all iterations of the loop.
    gaps = []
    for i in range(x):
        next_elem = a[(i + 1) % x] + (n if i == x - 1 else 0)
        
        gap = next_elem - a[i] - 1
        
        if gap > 0:
            gaps.append(gap)
        
    #State: n is an integer between 4 and 10^9, x is an integer between 2 and min(n, 2 * 10^5) and must be greater than 0, y is an integer between 0 and n - x, a is a sorted list of x distinct integers between 0 and n-1, present is a set containing the unique elements of a, stdin is empty, i is x, t1 is an integer equal to (a[x-1] + 1) % n, t2 is an integer equal to (a[x-1] + 2) % n, ans is an integer equal to x - 2 + k, where k is the number of times t1 is not in present and t2 is in present for all iterations of the loop, gaps is a list containing all the gaps between consecutive elements in the list a, next_elem is an integer equal to a[0] + (n if i == x - 1 else 0), and gap is an integer equal to next_elem - a[x-1] - 1.
    gaps.sort()
    for gap in gaps:
        pairs = gap // 2
        
        if y >= pairs:
            ans += gap
            y -= pairs
        else:
            ans += 2 * y
            break
        
    #State: n is an integer between 4 and 10^9, x is an integer between 2 and min(n, 2 * 10^5) and must be greater than 0, y is an integer between 0 and n - x, a is a sorted list of x distinct integers between 0 and n-1, present is a set containing the unique elements of a, i is x, t1 is an integer equal to (a[x-1] + 1) % n, t2 is an integer equal to (a[x-1] + 2) % n, ans is an integer equal to x - 2 + k + sum(gaps) if y is greater than or equal to sum(pairs), otherwise ans is an integer equal to x - 2 + k + 2y + sum(gaps[:j]) where j is the smallest index such that y < pairs[j], where k is the number of times t1 is not in present and t2 is in present for all iterations of the loop, gaps is an empty list, next_elem is an integer equal to a[0] + (n if i == x - 1 else 0), and pairs is an empty list.
    print(ans)
    #This is printed: ans (where ans is the calculated value based on the given conditions and variables)

#Overall this is what the function does:Calculates and prints the maximum number of pairs that can be formed from a given set of integers, considering certain conditions and constraints. The function takes no arguments and reads input from stdin, processing multiple test cases. It calculates the maximum number of pairs by analyzing the gaps between consecutive elements in the input list and the available pairs, and prints the result.

