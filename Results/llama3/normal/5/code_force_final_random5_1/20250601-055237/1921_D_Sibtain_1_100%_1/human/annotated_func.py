#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three lines. The first line contains two integers n and m (1 ≤ n ≤ m ≤ 2 * 10^5). The second line contains n integers a_i (1 ≤ a_i ≤ 10^9). The third line contains m integers b_i (1 ≤ b_i ≤ 10^9).
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
        
    #State: `_` is equal to the number of test cases, `n` is an integer, `m` is an integer, `a` is a sorted list of integers, `c` is a sorted list of integers in reverse order, `k` is equal to the length of `a`, `ans` is the sum of the maximum of the absolute differences between the elements of `a` and `c` at indices `i` and `j` and the absolute differences between the elements of `a` and `c` at indices `len(a) - j` and `len(c) - j`, `t1` is the absolute difference between the `i`-th element of the sorted list `a` and the `i`-th element of the sorted list `c`, `t2` is the absolute difference between the `(len(a) - j)`-th element of the sorted list `a` and the `(len(c) - j)`-th element of the sorted list `c`, `i` is equal to the length of `a`, `j` is equal to the length of `a` plus 1, stdin is empty, and the calculated answer is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines: two integers n and m, followed by n integers a_i and m integers b_i. It then calculates the sum of the maximum absolute differences between corresponding elements in the sorted lists a and c (in reverse order), with the exception of the case where all elements in both lists are equal, in which case it prints 0. The function prints the calculated sum for each test case.

