#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of two integers n and m (1 <= n, m <= 2 * 10^5) followed by two binary strings a and b of lengths n and m, respectively.
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
        
    #State: Output State: The value of k is the number of matching characters between strings a and b, and the value of j is the index of the last matched character in string b plus one. The value of i is n, and the values of t, n, m, a, and b remain unchanged.
    print(k)
    #This is printed: k (where k is the number of matching characters between strings a and b)

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the number of matching characters between two binary strings a and b. It takes no arguments and returns no value, but rather prints the result directly. The input is expected to be in a specific format, with an integer t followed by t test cases, each consisting of two integers n and m, and two binary strings a and b. The function then iterates through string a and string b, counting the number of matching characters and keeping track of the index of the last matched character in string b. Finally, it prints the count of matching characters.

