#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t test cases. Each test case consists of two lines. The first line contains two integers n and k (1 <= n <= 100, 2 <= k <= 100). The second line contains n integers c_1, c_2, ..., c_n (1 <= c_i <= 100).
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        p = [l.count(j) for j in set(l)]
        
        if max(p) >= k:
            print(k - 1)
        else:
            print(n)
        
    #State: Output State: The output state after the loop executes all the iterations is a series of printed values, each representing the minimum number of operations required to make all elements in the list equal to the most frequent element. If the maximum frequency of any element is greater than or equal to k, the output is k-1; otherwise, the output is n, the number of elements in the list. The value of t, the number of test cases, remains unchanged, as it is not affected by the loop.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the minimum number of operations required to make all elements in a list equal to the most frequent element. For each test case, it reads two integers (n and k) and a list of n integers, then calculates the frequency of each unique element in the list. If the maximum frequency is greater than or equal to k, it prints k-1; otherwise, it prints n, the number of elements in the list. The function processes all test cases and prints the results accordingly.

