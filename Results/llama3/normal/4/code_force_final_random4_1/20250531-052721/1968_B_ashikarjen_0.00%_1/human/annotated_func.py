#State of the program right berfore the function call: stdin contains t test cases. Each test case contains three lines. The first line contains two space-separated integers n and m. The second and third lines contain two binary strings a and b of lengths n and m, respectively.
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
        
    #State: `k` is the number of times `a[i]` is found in `b`, `j` is equal to `m`, `i` is equal to `n`.
    print(k)
    #This is printed: the number of times a[n] is found in b

#Overall this is what the function does:This function reads input from stdin for a specified number of test cases, where each test case consists of two binary strings a and b of lengths n and m, respectively. It then searches for occurrences of characters from string a in string b and prints the total count of found occurrences. The function does not modify the input strings and only outputs the count of found occurrences.

