#State of the program right berfore the function call: stdin contains t test cases. Each test case contains three inputs: two integers n and m, and two binary strings a and b. n and m are non-negative integers such that 0 <= n <= 2*10^5 and 0 <= m <= 2*10^5. The length of a is n and the length of b is m.
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
        
    #State: Output State: The value of k is the number of matching characters between the strings a and b, and the value of j is the index of the last matched character in string b plus one. The values of t, n, m, a, and b remain unchanged.
    print(k)
    #This is printed: k (where k is the number of matching characters between the strings a and b)

#Overall this is what the function does:This function reads input from stdin, containing a test case with two integers (n and m) and two binary strings (a and b). It then compares the strings a and b, counting the number of matching characters. The function prints the count of matching characters to the console, leaving the input values unchanged.

