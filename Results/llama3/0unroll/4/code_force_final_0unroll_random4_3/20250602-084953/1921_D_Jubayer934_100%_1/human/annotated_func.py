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
        
    #State: The sum of the minimum absolute differences between the corresponding elements of the two lists a and b for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lists of integers, a and b. It calculates the sum of the minimum absolute differences between corresponding elements of the two lists, either by comparing elements at the same index or by comparing elements at mirrored indices (i.e., the first element of a with the last element of b, the second element of a with the second-to-last element of b, and so on). The function prints the sum of these minimum absolute differences for each test case.

