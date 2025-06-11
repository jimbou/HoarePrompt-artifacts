#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three lines. The first line contains two integers n and m (1 <= n <= m <= 2 * 10^5). The second line contains n integers a_i (1 <= a_i <= 10^9). The third line contains m integers b_i (1 <= b_i <= 10^9).
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        temp = -1
        
        ans = []
        
        a = sorted(map(int, input().split()))[:n]
        
        b = sorted(map(int, input().split()), reverse=True)[:m]
        
        for i in range(n):
            if abs(a[i] - b[-(n - i)]) > abs(a[i] - b[i]):
                temp = i
                break
            ans.append(abs(a[i] - b[i]))
        
        if temp != -1:
            for i in range(temp, n):
                ans.append(abs(a[i] - b[-(n - i)]))
        
        print(sum(ans))
        
    #State: `_` is equal to the number of test cases, `stdin` is empty, `i` is equal to `n`, `ans` is a list containing the absolute differences between the first min(n, m) elements of `a` and `b` if `temp` is -1, or a list containing the absolute differences between the first min(n, m) elements of `a` and `b` and the absolute differences between `a[i - (n - temp - 1)]` and `b[-(n - (i - (n - temp - 1)))]` and ... and the absolute difference between `a[i - 1]` and `b[-(n - (i - 1))]` and the absolute difference between `a[i]` and `b[-(n - i)]` if `temp` is not -1, and the sum of the absolute differences is printed for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines: two integers n and m, followed by n integers a_i and m integers b_i. It calculates the sum of absolute differences between the first min(n, m) elements of a_i and b_i, and if a certain condition is met, it also calculates the sum of absolute differences between the remaining elements of a_i and the corresponding elements of b_i in reverse order. The function prints the sum of these absolute differences for each test case, and after processing all test cases, the standard input is empty.

