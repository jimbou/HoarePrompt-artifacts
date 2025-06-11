#State of the program right berfore the function call: stdin contains two inputs: first an integer n (3 <= n <= 3*10^5) and then a string a of length n, consisting only of 0 and 1.
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
        
    #State: Output State: n is an integer between 3 and 3*10^5, a is a string of length n consisting only of 0 and 1, S is a list containing n+1 lists, each with two elements, the first element of each list is the count of '0's in the substring of a from the start to the current position, the second element of each list is the count of '1's in the substring of a from the start to the current position, stdin is empty
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
        
    #State: Output State: The value of ans is the index i that minimizes the absolute difference between n/2 and i, subject to the condition that the number of 0's on the left side of the string is at least half the total number of 0's and 1's on the left side, and the number of 1's on the right side of the string is at least half the total number of 0's and 1's on the right side. The values of n, a, S, satisfy, and stdin remain unchanged.
    print(ans)
    #This is printed: the index i that minimizes the absolute difference between n/2 and i, subject to the condition that the number of 0's on the left side of the string is at least half the total number of 0's and 1's on the left side, and the number of 1's on the right side of the string is at least half the total number of 0's and 1's on the right side

#Overall this is what the function does:This function reads an integer n and a string a of length n from standard input, where a consists only of 0 and 1. It then calculates the cumulative counts of 0 and 1 in the string and finds the index i that minimizes the absolute difference between n/2 and i, subject to the condition that the number of 0's on the left side of the string is at least half the total number of 0's and 1's on the left side, and the number of 1's on the right side of the string is at least half the total number of 0's and 1's on the right side. The function prints this index i to standard output.

#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer and then a string of 0s and 1s of the same length as the integer.
    for _ in range(int(input())):
        func_1()
        
    #State: stdin contains multiple test cases. Each test case contains two inputs: first an integer and then a string of 0s and 1s of the same length as the integer. The loop has executed all the iterations.

#Overall this is what the function does:Executes a specified number of iterations of a function, func_1, based on input from stdin, without modifying the input or producing any output.

