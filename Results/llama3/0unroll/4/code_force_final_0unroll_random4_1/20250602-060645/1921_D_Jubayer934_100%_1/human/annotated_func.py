#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three lines. The first line contains two space-separated integers n and m (1 <= n <= m <= 2 * 10^5). The second line contains n space-separated integers a_i (1 <= a_i <= 10^9). The third line contains m space-separated integers b_i (1 <= b_i <= 10^9).
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
        
    #State: The output state after the loop executes all the iterations is the sum of the minimum absolute differences between the corresponding elements of the two sorted lists, a and b, for each test case. The output is a single integer value for each test case, representing the total sum of these minimum absolute differences.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lists of integers. It calculates the sum of the minimum absolute differences between corresponding elements of the two sorted lists, with the option to swap elements from the second list in reverse order if it results in a smaller difference. The function then prints the total sum of these minimum absolute differences for each test case.

