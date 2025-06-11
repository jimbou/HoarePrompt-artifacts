#State of the program right berfore the function call: stdin contains a number of test cases t, followed by t test cases. Each test case consists of three integers n, m, and k, followed by a list of n integers a, and a list of m integers b. n, m, and k are positive integers such that k <= m <= n. The elements of a and b are positive integers not greater than 10^6.
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
        
    #State: t is 0, n is a positive integer, m is a positive integer that is less than n, k is a positive integer, a is a list of n positive integers not greater than 10^6, j is m, r is n, ans is the number of times the number of elements in done is greater than or equal to k, extra contains all elements of a that were not in todo initially and contains all elements of a that were in todo initially but were removed from done, todo is empty if a[n-1] is not in done, otherwise todo contains a[n-1], and done contains all elements of a that were in todo initially and were not removed from done, and the number of times the number of elements in done is greater than or equal to k is printed.

#Overall this is what the function does:This function reads a number of test cases from standard input, where each test case consists of three integers (n, m, k) and two lists of integers (a and b). It then processes the test cases, maintaining sets of "done" and "extra" elements, and counts the number of times the number of "done" elements is greater than or equal to k. Finally, it prints the count for each test case.

