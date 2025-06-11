#State of the program right berfore the function call: stdin contains two inputs: first an integer n and then a string a of length n, consisting only of 0 and 1.
    n = int(input())
    a = input()
    S = [[0, 0]]
    for s in a:
        x, y = S[-1]
        
        if s == '0':
            x += 1
        else:
            y += 1
        
        S.append([x, y])
        
    #State: Output State: n is an integer, a is a string of length n consisting only of 0 and 1, S is a list containing n+1 lists, where each list contains two elements: the count of 0s and the count of 1s in the corresponding prefix of a, stdin is empty
    ans = -1
    for i in range(n + 1):
        left = S[i][0]
        
        lsum = i
        
        right = S[-1][1] - S[i][1]
        
        rsum = n - i
        
        if left * 2 < lsum or right * 2 < rsum:
            continue
        elif abs(n / 2 - i) < abs(n / 2 - ans):
            ans = i
        
    #State: Output State: `ans` is the index `i` that minimizes the absolute difference between `n/2` and `i`, subject to the conditions `left * 2 >= lsum` and `right * 2 >= rsum`, where `left` is the count of 0s in the prefix of `a` up to index `i`, `lsum` is the length of the prefix up to index `i`, `right` is the count of 1s in the suffix of `a` starting from index `i+1`, and `rsum` is the length of the suffix starting from index `i+1`.
    print(ans)
    #This is printed: the index i that minimizes the absolute difference between n/2 and i, subject to the conditions left * 2 >= lsum and right * 2 >= rsum

#Overall this is what the function does:This function reads an integer n and a string a of length n from standard input, where a consists only of 0s and 1s. It then calculates the count of 0s and 1s in all prefixes of a and stores them in a list S. The function then iterates over the list S to find the index i that minimizes the absolute difference between n/2 and i, subject to the conditions that the count of 0s in the prefix up to index i is at least half the length of the prefix, and the count of 1s in the suffix starting from index i+1 is at least half the length of the suffix. If such an index is found, the function prints it; otherwise, it prints -1.

#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer and then a string of 0s and 1s of the same length as the integer.
    for _ in range(int(input())):
        func_1()
        
    #State: stdin is empty

#Overall this is what the function does:Reads multiple test cases from standard input, where each test case consists of an integer and a string of 0s and 1s of the same length, and processes each test case using the func_1 function, leaving the standard input empty after all test cases have been processed.

