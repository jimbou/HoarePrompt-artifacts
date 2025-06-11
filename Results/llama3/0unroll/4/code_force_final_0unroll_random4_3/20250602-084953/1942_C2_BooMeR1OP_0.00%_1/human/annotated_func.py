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
        
    #State: Output State: The value of ans has been updated to be the number of elements in the list a that are one less than a multiple of n and two more than another element in the list a. The value of t1 and t2 are the last values calculated in the loop, which are (a[x-1] + 1) % n and (a[x-1] + 2) % n respectively. The values of all other variables remain unchanged.
    gaps = []
    for i in range(x):
        next_elem = a[(i + 1) % x] + (n if i == x - 1 else 0)
        
        gap = next_elem - a[i] - 1
        
        if gap > 0:
            gaps.append(gap)
        
    #State: Output State: The value of ans remains unchanged. The value of t1 is (a[x-1] + 1) % n and the value of t2 is (a[x-1] + 2) % n. The list gaps contains the differences between consecutive elements in the list a, minus 1, but only if the difference is greater than 0. The values of all other variables remain unchanged.
    gaps.sort()
    for gap in gaps:
        pairs = gap // 2
        
        if y >= pairs:
            ans += gap
            y -= pairs
        else:
            ans += 2 * y
            break
        
    #State: Output State: The value of ans is increased by the sum of all gaps in the list gaps, but only up to the number of pairs that can be formed from each gap, which is gap // 2. If y is greater than or equal to the number of pairs that can be formed from a gap, then the entire gap is added to ans and y is decreased by the number of pairs. If y is less than the number of pairs that can be formed from a gap, then 2 times y is added to ans and the loop breaks. The value of t1 remains (a[x-1] + 1) % n and the value of t2 remains (a[x-1] + 2) % n. The list gaps remains unchanged. The values of all other variables remain unchanged.
    print(ans)
    #This is printed: the value of ans which is increased by the sum of all gaps in the list gaps, but only up to the number of pairs that can be formed from each gap, which is gap // 2

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the result. It accepts no parameters and returns no value. The function reads an integer t, followed by t test cases. Each test case consists of three integers n, x, and y, and a list of x distinct integers. The function calculates the number of elements in the list that are one less than a multiple of n and two more than another element in the list, and then calculates the differences between consecutive elements in the list, minus 1, but only if the difference is greater than 0. It then increases the count by the sum of all gaps, but only up to the number of pairs that can be formed from each gap. Finally, it prints the updated count.

