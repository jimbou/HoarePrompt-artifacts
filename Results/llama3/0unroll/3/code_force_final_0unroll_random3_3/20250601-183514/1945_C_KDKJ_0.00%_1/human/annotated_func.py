#State of the program right berfore the function call: stdin contains two inputs: first an integer and then a string of '0' and '1' of the same length as the integer.
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
        
    #State: Output State: n is an integer, a is a string of '0' and '1' of length n, S is a list of n+1 pairs of integers, where the first pair is [0, 0] and each subsequent pair is the sum of the previous pair and [1, 0] if the corresponding character in a is '0', or [0, 1] if the corresponding character in a is '1', stdin is empty.
    ans = 0
    satisfy = 0
    for i in range(n):
        left = S[i][0]
        
        lsum = S[i][0] + S[i][1]
        
        right = S[-1][1] - S[i][1]
        
        rsum = n - lsum
        
        if left * 2 < lsum or right * 2 < rsum:
            continue
        elif abs(n / 2 - i) <= abs(n / 2 - ans):
            ans = i
        
    #State: Output State: The final value of ans is the index i in the string a that is closest to the middle of the string and has the property that the number of '1's to the left of i is at least half the total number of '1's to the left of i, and the number of '1's to the right of i is at least half the total number of '1's to the right of i. If no such index exists, ans remains 0. The values of n, a, S, stdin, and satisfy remain unchanged.
    print(ans)
    #This is printed: the index i in the string a that is closest to the middle of the string and has the property that the number of '1's to the left of i is at least half the total number of '1's to the left of i, and the number of '1's to the right of i is at least half the total number of '1's to the right of i, or 0 if no such index exists

#Overall this is what the function does:This function reads an integer and a string of '0' and '1' from standard input, then finds the index in the string that is closest to the middle and has the property that the number of '1's to the left of it is at least half the total number of '1's to the left of it, and the number of '1's to the right of it is at least half the total number of '1's to the right of it. If no such index exists, it returns 0. The function prints the result to standard output.

#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer and then a string of 0s and 1s of length equal to the integer.
    for _ in range(int(input())):
        func_1()
        
    #State: stdin is empty.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer and a string of 0s and 1s of equal length, and processes them without returning any output, leaving the standard input empty.

