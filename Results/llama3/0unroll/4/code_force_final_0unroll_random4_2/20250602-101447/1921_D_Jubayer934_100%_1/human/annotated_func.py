#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three lines: the first line contains two integers n and m (1 ≤ n ≤ m ≤ 2 * 10^5), the second line contains n integers a_i (1 ≤ a_i ≤ 10^9), and the third line contains m integers b_i (1 ≤ b_i ≤ 10^9).
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
        
    #State: The sum of the minimum absolute differences between each pair of elements from the two sorted arrays, for each test case.

#Overall this is what the function does:For each test case, the function calculates the sum of the minimum absolute differences between each pair of elements from two sorted arrays, a and b, where the pairs are formed by either matching elements at the same index or matching elements at mirrored indices (i.e., the first element of a with the last element of b, the second element of a with the second last element of b, and so on), whichever results in a smaller absolute difference. The function then prints the sum of these minimum absolute differences for each test case.

