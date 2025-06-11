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
        
    #State: j is equal to m, n is an integer between 1 and 2 * 10^5, m is an integer between 1 and 2 * 10^5, a is a binary string of length n, b is a binary string of length m, k is an integer between 0 and n, i is equal to n, stdin contains t-1 test cases if n is equal to 0, otherwise stdin contains t-2 test cases.
    print(k)
    #This is printed: k (where k is an integer between 0 and n)

#Overall this is what the function does:This function reads two binary strings from standard input and prints the maximum number of matching characters that can be found in the second string when iterating through the first string from left to right, without reusing any characters in the second string. It repeats this process for a specified number of test cases, also read from standard input.

