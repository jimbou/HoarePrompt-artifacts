#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three lines. The first line contains three integers n, m, and k. The second line contains n integers a_1, a_2, ..., a_n. The third line contains m integers b_1, b_2, ..., b_m. 1 <= n, m, k <= 2 * 10^5, 1 <= k <= m <= n, 1 <= a_i, b_i <= 10^6.
    for _ in range(int(input())):
        n, m, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        todo = set(map(int, input().split()))
        
        done = set()
        
        extra = set()
        
        for j in range(m):
            if a[j] in todo:
                todo.remove(a[j])
                done.add(a[j])
            else:
                extra.add(a[j])
        
        ans = 1 if len(done) >= k else 0
        
        for r in range(m, n):
            old = a[r - m]
            if old in extra:
                extra.remove(old)
            elif old in done:
                done.remove(old)
                todo.add(old)
            if a[r] in todo:
                todo.remove(a[r])
                done.add(a[r])
            else:
                extra.add(a[r])
            if len(done) >= k:
                ans += 1
        
        print(ans)
        
    #State: The output state will contain the number of times the condition len(done) >= k is met for each test case, printed on a new line for each test case.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of three lines: the first line contains three integers n, m, and k, the second line contains n integers a_1 to a_n, and the third line contains m integers b_1 to b_m. The function then determines the number of times a condition is met, where the condition is that at least k elements from the set of m integers b_1 to b_m are found within a sliding window of size m in the list of n integers a_1 to a_n. The function prints the count of times this condition is met for each test case.

