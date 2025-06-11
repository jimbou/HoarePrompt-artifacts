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
        
    #State: t is an integer between 1 and 500 inclusive, i is t - 1, n is an integer, k is an integer, l is a list of integers, p is a list of integers representing the frequency of each unique integer in l, stdin is empty. If the maximum frequency of any integer in l is greater than or equal to k, then the value of k - 1 is printed. Otherwise, the value of n is printed.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the minimum number of operations required to make all elements in a list unique. It accepts no parameters and returns no value. The function reads an integer t, representing the number of test cases, followed by t test cases. Each test case consists of two integers n and k, and a list of n integers. The function calculates the frequency of each unique integer in the list and prints k-1 if the maximum frequency is greater than or equal to k, otherwise, it prints n. The function processes all test cases and leaves stdin empty.

