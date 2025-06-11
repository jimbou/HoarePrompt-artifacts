#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three lines. The first line contains two integers n and m (1 <= n <= m <= 2 * 10^5). The second line contains n integers a_i (1 <= a_i <= 10^9). The third line contains m integers b_i (1 <= b_i <= 10^9).
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
        
    #State: `n` is an integer, `m` is an integer, `a` is a sorted list of integers, `c` is a sorted list of integers in reverse order, `_` is equal to the number of test cases, stdin is empty, `k` is equal to the length of `a`, `t1` is the absolute difference between the last element of the sorted list `a` and the last element of the sorted list `c` in reverse order, `t2` is the absolute difference between the first element of the sorted list `a` and the first element of the sorted list `c` in reverse order, `ans` is the sum of the maximum of `t1` and `t2` for all iterations, `i` is equal to the length of `a`, `j` is equal to the length of `c`, and the total maximum absolute difference between the elements of `a` and `c` which is `ans` has been printed for all test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines: two integers n and m, followed by n integers a_i and m integers b_i. It then calculates and prints the maximum absolute difference between the elements of a_i and b_i for each test case, considering all possible pairings of elements from the two lists. If the lists contain only one element or all elements are the same, it prints the absolute difference between the single element and the closest element in the other list. The function processes all test cases and prints the results, leaving the standard input empty.

