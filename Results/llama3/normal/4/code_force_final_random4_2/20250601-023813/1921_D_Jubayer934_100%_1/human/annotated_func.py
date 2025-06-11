#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three lines. The first line contains two integers n and m (1 ≤ n ≤ m ≤ 2 × 10^5). The second line contains n integers a_i (1 ≤ a_i ≤ 10^9). The third line contains m integers b_i (1 ≤ b_i ≤ 10^9).
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
        
    #State: The loop has executed for all the test cases in the input. The values of `n`, `m`, `a`, `b`, `i`, `ans`, and `temp` have been updated according to the last test case. The sum of the absolute differences between the elements of `a` and the corresponding elements of `b` has been printed for each test case. The input has been fully consumed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three lines: two integers n and m, followed by n integers and m integers. It calculates the sum of the absolute differences between the elements of the two sets of integers, with a specific pairing strategy. If the absolute difference between an element in the first set and the corresponding element in the second set is greater than the absolute difference between the element in the first set and the element in the second set that is mirrored from the end, it switches to a mirrored pairing strategy for the remaining elements. The function prints the sum of the absolute differences for each test case and consumes the entire input.

