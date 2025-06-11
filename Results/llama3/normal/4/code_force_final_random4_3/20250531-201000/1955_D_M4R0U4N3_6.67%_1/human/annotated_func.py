#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers n, m, and k, followed by a list of n integers a_1, a_2, ..., a_n, and a list of m integers b_1, b_2, ..., b_m. 1 <= k <= m <= n <= 2 * 10^5. 1 <= a_i, b_i <= 10^6.
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
        
    #State: n is an integer, m is an integer that is less than n, k is an integer, a is a list of integers, todo is a set of integers, done is a set of integers, extra is a set of integers, _ is the number of test cases, j is m, r is n, ans is the number of elements in done that are greater than or equal to k, stdin is empty. If the element at index r - m of a is in extra, then extra does not include the element at index r - m of a. Otherwise, if the element at index r - m of a is in done, then todo includes the element at index r - m of a and done does not include the element at index r - m of a. Otherwise, todo does not include the element at index r - m of a and done includes the element at index r - m of a. The element at index r of a is either in done or extra, and the number of elements in done that are greater than or equal to k is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three integers (n, m, k) and two lists of integers (a and b). It then processes the lists to determine the number of elements in the first list (a) that are present in the second list (b) within a sliding window of size m. The function prints the count of such elements for each test case.

