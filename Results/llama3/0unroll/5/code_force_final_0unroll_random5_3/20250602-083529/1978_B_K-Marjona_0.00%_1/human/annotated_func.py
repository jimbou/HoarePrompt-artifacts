#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^4). Each of the following t lines contains three integers n, a, and b (1 <= n, a, b <= 10^9).
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print((b + (b - k + 1)) // 2 * k + (n - k) * a)
        
    #State: The output state is a list of integers, each representing the maximum sum of n integers in the range [a, b] that can be obtained by selecting k integers from the range [a, b] and the remaining (n-k) integers from the range [a, a+k-1]. The list contains t integers, where t is the number of test cases.

#Overall this is what the function does:This function reads multiple lines of input from stdin, where the first line contains the number of test cases (t) and each subsequent line contains three integers (n, a, b) representing the number of integers, the start of the range, and the end of the range, respectively. It then calculates and prints the maximum sum of n integers that can be obtained by selecting k integers from the range [a, b] and the remaining (n-k) integers from the range [a, a+k-1], where k is the minimum of n and (b - a). If b is less than or equal to a, it simply prints the product of a and n. The function repeats this process for each test case and outputs a list of integers representing the maximum sum for each case.

