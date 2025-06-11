#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of two integers n and m (1 <= n, m <= 2 * 10^5) followed by two binary strings a and b of lengths n and m respectively.
    n, m = map(int, input().split())
    a = input()
    b = input()
    k = 0
    j = 0
    for i in range(n):
        while j < m and b[j] != a[i]:
            j += 1
        
        if j < m:
            k += 1
            j += 1
        else:
            break
        
    #State: Output State: The value of k is the length of the longest common subsequence of a and b, and the value of j is the index of the last character in b that is part of this subsequence. The values of t, n, m, a, and b remain unchanged.
    print(k)
    #This is printed: the length of the longest common subsequence of a and b

#Overall this is what the function does:This function reads input from stdin, where the first line contains an integer t (1 <= t <= 10^4) representing the number of test cases. For each test case, it reads two integers n and m (1 <= n, m <= 2 * 10^5) and two binary strings a and b of lengths n and m respectively. It then calculates and prints the length of the longest common subsequence of a and b. The function does not modify the input values t, n, m, a, and b.

