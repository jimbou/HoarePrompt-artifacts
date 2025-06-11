#State of the program right berfore the function call: stdin contains t test cases. Each test case contains three lines. The first line contains two space-separated integers n and m. The second line contains a binary string a of length n. The third line contains a binary string b of length m.
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
        
    #State: `n` is an integer, `m` is an integer, `a` is a binary string of length `n`, `b` is a binary string of length `m`, `k` is the number of times a character in `a` is found in `b`, `j` is equal to `m`, `i` is equal to `n`.
    print(k)
    #This is printed: k (where k is the number of times a character in a is found in b)
    return
    #The program returns nothing. The number of times a character in `a` is found in `b` which is `k` has been printed. The value of `j` is equal to `m` and the value of `i` is equal to `n`.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the number of times a character in a binary string `a` is found in another binary string `b`. It accepts no parameters and returns nothing, only printing the result to the console. The function iterates through each character in `a` and checks if it exists in `b`, incrementing a counter `k` each time a match is found. The function concludes by printing the value of `k`, which represents the total number of matches found.

