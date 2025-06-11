#State of the program right berfore the function call: stdin contains t test cases. Each test case contains three inputs: two integers n and m, and two binary strings a and b of length n and m respectively.
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
        
    #State: `n` is an integer greater than or equal to 0, `m` is an integer greater than or equal to 0, `a` is a binary string of length `n`, `b` is a binary string of length `m`, `k` is the number of times `a[i]` is found in `b` for `i` in range `n`, `i` is `n`, `j` is `m`, and stdin contains t-1 test cases.
    print(k)
    #This is printed: k (where k is the count of occurrences of each character in a within the string b)

#Overall this is what the function does:This function reads two integers and two binary strings from standard input, then counts and prints the number of occurrences of each character in the first string within the second string, effectively performing a substring matching operation. It processes one test case at a time, with multiple test cases provided in the input.

