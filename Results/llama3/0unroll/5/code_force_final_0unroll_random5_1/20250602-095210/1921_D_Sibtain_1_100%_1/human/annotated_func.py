#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three lines: the first line contains two integers n and m (1 <= n <= m <= 2 * 10^5), the second line contains n integers a_i (1 <= a_i <= 10^9), and the third line contains m integers b_i (1 <= b_i <= 10^9).
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
        
    #State: The output state will contain the minimum total absolute difference between the elements of the two arrays for each test case, one on each line.

#Overall this is what the function does:This function calculates and prints the minimum total absolute difference between the elements of two arrays for each test case. It accepts multiple test cases as input, where each test case consists of two arrays, and returns the minimum total absolute difference for each test case. The function handles various cases, including when the arrays have identical elements, when one array has a single element, and when the arrays have distinct elements. It outputs the minimum total absolute difference for each test case, one on each line.

