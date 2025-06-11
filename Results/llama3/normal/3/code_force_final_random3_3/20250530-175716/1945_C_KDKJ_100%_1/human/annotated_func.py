#State of the program right berfore the function call: stdin contains two inputs: first an integer n (n >= 3) and then a string a of length n, consisting only of 0 and 1.
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
        
    #State: n is an integer greater than or equal to 3, a is an empty string, S is a list containing n+1 lists, the first list contains two elements, both 0, the rest of the lists contain two elements, x and y, where x is the number of '0's in the original string a and y is the number of '1's in the original string a, stdin is empty.
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
        
    #State: n is an integer greater than or equal to 3, a is an empty string, S is a list containing n+1 lists, the first list contains two elements, both 0, the rest of the lists contain two elements, x and y, where x is the number of '0's in the original string a and y is the number of '1's in the original string a, ans is the integer closest to n/2, stdin is empty, i is n.
    print(ans)
    #This is printed: the integer closest to n/2 (where n is an integer greater than or equal to 3)

#Overall this is what the function does:This function reads two inputs from the standard input: an integer n (n >= 3) and a string a of length n consisting only of 0 and 1. It then processes the string to find the integer closest to n/2 and prints this value. The function does not modify the input variables and does not return any value, only printing the result.

#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer and then a string of 0 and 1. The integer is a positive integer greater than or equal to 3 and less than or equal to 3*10^5. The length of the string is equal to the integer.
    for _ in range(int(input())):
        func_1()
        
    #State: _ is int(input()) - 1, stdin contains no more test cases, and a function named func_1 has been executed int(input()) times.

#Overall this is what the function does:Executes a function named func_1 for a specified number of test cases read from standard input, where each test case consists of an integer and a string of 0s and 1s, and consumes all test cases from standard input.

