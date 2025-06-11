#State of the program right berfore the function call: stdin contains two inputs: first an integer n (n >= 3) and then a string a of length n consisting only of 0 and 1.
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
        
    #State: Output State: n is an integer greater than or equal to 3, a is a string of length n consisting only of 0 and 1, S is a list containing n+1 lists, where the first list contains 0 and 0, and each subsequent list contains the cumulative count of 0s and 1s in the string a up to that point, stdin is empty
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
        
    #State: Output State: `ans` is the index of the string `a` that is closest to the middle of the string and has a cumulative count of 0s and 1s that is closest to half the length of the string.
    print(ans)
    #This is printed: ans (where ans is the index of the string a that is closest to the middle of the string and has a cumulative count of 0s and 1s that is closest to half the length of the string)

#Overall this is what the function does:This function reads an integer n and a string a of length n from standard input, where a consists only of 0s and 1s. It calculates the cumulative count of 0s and 1s in the string and finds the index closest to the middle of the string where the cumulative count of 0s and 1s is closest to half the length of the string. The function then prints this index.

#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer and then a string of 0s and 1s. The integer is a positive integer and represents the length of the string.
    for _ in range(int(input())):
        func_1()
        
    #State: stdin is empty.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of a positive integer followed by a string of 0s and 1s. The function processes each test case, but the specific actions performed on each test case are not specified. After processing all test cases, the function leaves the standard input empty.

