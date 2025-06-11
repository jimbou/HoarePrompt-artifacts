#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three lines. The first line contains two space-separated integers n and m (1 ≤ n ≤ m ≤ 2 × 10^5). The second line contains n space-separated integers a_i (1 ≤ a_i ≤ 10^9). The third line contains m space-separated integers b_i (1 ≤ b_i ≤ 10^9).
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        c = list(map(int, input().split()))
        
        if len(set(a)) == 1 and len(set(c)) == 1 and a[0] == c[0]:
            print(0)
            continue
        
        a.sort()
        
        c.sort(reverse=True)
        
        if len(a) == 1:
            print(max(abs(a[0] - max(c)), abs(a[0] - min(c))))
            continue
        
        i, j, ans = 0, 1, 0
        
        for k in range(len(a)):
            t1 = abs(a[i] - c[i])
            t2 = abs(a[len(a) - j] - c[len(c) - j])
            if t2 > t1:
                j += 1
            else:
                i += 1
            ans += max(t1, t2)
        
        print(ans)
        
    #State: The output state after the loop executes all the iterations will be the sum of the maximum absolute differences between the corresponding elements of the two sorted lists, a and c, for each test case. The maximum absolute difference is calculated by comparing the absolute differences between the elements at the current positions in the two lists and the elements at the mirrored positions from the ends of the lists. The output will be a list of these sums, one for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines: two integers n and m, followed by n integers a_i and m integers b_i. It then calculates and prints the sum of the maximum absolute differences between corresponding elements of the two sorted lists a and c for each test case. If the lists contain identical elements, it prints 0. If a list contains only one element, it prints the maximum absolute difference between that element and the maximum or minimum element of the other list. Otherwise, it iterates through the lists, comparing absolute differences between elements at current and mirrored positions, and prints the sum of these maximum differences.

