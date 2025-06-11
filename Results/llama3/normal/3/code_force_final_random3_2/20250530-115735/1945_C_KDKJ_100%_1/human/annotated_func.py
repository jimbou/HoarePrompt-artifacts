#State of the program right berfore the function call: n is a positive integer greater than or equal to 3 and a is a string of length n consisting only of '0' and '1'.
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
        
    #State: n is an integer greater than or equal to 0, a is an empty string, S is a list containing n+1 lists: the first list contains two elements: 0 and 0, the rest of the lists contain two elements: x and y, where x is the number of '0's in the string a and y is the number of '1's in the string a, stdin is empty.
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
        
    #State: n is an integer greater than or equal to 0, a is an empty string, S is a list containing n+1 lists: the first list contains two elements: 0 and 0, the rest of the lists contain two elements: x and y, where x is the number of '0's in the string a and y is the number of '1's in the string a, stdin is empty, ans is the value of i that is closest to n/2.
    print(ans)
    #This is printed: the value of i that is closest to n/2 (where n is an integer greater than or equal to 0)

#Overall this is what the function does:This function reads a positive integer n and a string a of length n consisting only of '0' and '1' from the standard input, then calculates and prints the index i that is closest to n/2, where i is the position in the string a that divides the string into two parts with the most balanced number of '0's and '1's. The function returns no value, only printing the result to the standard output.

#State of the program right berfore the function call: stdin contains multiple test cases, each test case contains two inputs: first an integer and then a string of 0s and 1s of the same length as the integer.
    for _ in range(int(input())):
        func_1()
        
    #State: stdin contains multiple test cases, each test case contains two inputs: the first input is a valid integer greater than 0, and the second input is a string of 0s and 1s of the same length as the integer, and the function `func_1()` has been executed for each test case.

#Overall this is what the function does:Executes the function `func_1()` for each test case in the input, where each test case consists of a positive integer and a binary string of the same length, without modifying the input or producing any output.

