#State of the program right berfore the function call: s is a string consisting of characters '<' and '>'.
    n = len(s)
    A = []
    idx_A = []
    for i in range(0, n):
        if s[i] == '>':
            if len(idx_A) == 0:
                A.append(0)
            else:
                x = A[len(A) - 1] + (i - idx_A[len(idx_A) - 1]) * len(idx_A)
                A.append(x)
            idx_A.append(i)
        
    #State: `s` is a string consisting of characters '<' and '>', `n` is the length of `s`, `A` is a list containing elements that represent the cumulative sum of the products of the differences between the indices of '>' characters and the length of `idx_A` at each iteration, and `idx_A` is a list containing the indices of all '>' characters in `s`.
    B = []
    idx_B = []
    for j in range(0, n):
        i = n - 1 - j
        
        if s[i] == '<':
            if len(idx_B) == 0:
                B.append(0)
            else:
                x = B[len(B) - 1] + (idx_B[len(B) - 1] - i) * len(idx_B)
                B.append(x)
            idx_B.append(i)
        
    #State: The loop has finished executing, and the final state is reached. The variable `j` has reached the value `n`, which is the length of the string `s`. The variable `i` has reached the value `-1`, which is out of the bounds of the string `s`. The list `idx_B` contains the indices of all '<' characters in the string `s` in reverse order. The list `B` contains the cumulative sum of the products of the differences between the indices of '<' characters and the length of `idx_B` at each iteration.
    l = 0
    r = len(B)
    for i in range(0, n):
        if s[i] == '>':
            if l < r:
                a = A[l]
                x = r - (l + 2)
                b = B[r - 1]
                if x >= 0:
                    b = b - B[x]
                    b = b - (idx_B[x] - idx_B[r - 1]) * (x + 1)
                b = b + (idx_B[r - 1] - i) * (l + 1)
                print(a * 2 + b * 2 + i + 1, end=' ')
            elif r == 0:
                print(n - i, end=' ')
            else:
                a = B[r - 1] + (idx_B[r - 1] - i) * r
                b = A[l - 1]
                if l - r > 0:
                    b = b - A[l - r - 1]
                    b = b - (idx_A[l - 1] - idx_A[l - r - 1]) * (l - r)
                b = b + (i - idx_A[l - 1]) * r
                print(a * 2 + b * 2 + (n - i), end=' ')
            l += 1
        else:
            r -= 1
            if l <= r:
                if l == 0:
                    print(i + 1, end=' ')
                else:
                    a = A[l - 1]
                    a = a + (i - idx_A[l - 1]) * l
                    b = B[r]
                    if r - l >= 0:
                        b = b - B[r - l]
                        b = b - (idx_B[r - l] - i) * (r - l)
                    b = b + (idx_B[r] - i) * l
                    print(a * 2 + b * 2 + i + 1, end=' ')
            elif r == 0:
                print(n - i + (i - idx_A[l - 1]) * 2, end=' ')
            else:
                a = B[r]
                b = A[l - 1]
                if l - r - 1 > 0:
                    b = b - A[l - r - 2]
                    b = b - (idx_A[l - 1] - idx_A[l - r - 2]) * (l - r - 1)
                b = b + (i - idx_A[l - 1]) * (r + 1)
                print(a * 2 + b * 2 + (n - i), end=' ')
        
    #State: i is n, j is n, idx_B contains the indices of all '<' characters in the string s in reverse order, B contains the cumulative sum of the products of the differences between the indices of '<' characters and the length of idx_B at each iteration, l is n, r is 0

#Overall this is what the function does:The function takes a string `s` consisting of '<' and '>' characters as input and prints the cumulative sum of products of differences between indices of '<' and '>' characters at each position, considering both forward and backward directions. It calculates the cumulative sum by iterating through the string twice, first from left to right and then from right to left, and uses two lists `A` and `B` to store the cumulative sums. The function prints the results for each position in the string, handling cases where the indices of '<' and '>' characters are at the boundaries of the string.

