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
        
    #State: n is an integer between 3 and 3*10^5, a is a string of length n consisting only of 0 and 1, S is a list containing n+1 lists: the first list contains two elements: 0 and 0, the rest of the lists contain two elements: x and y where x is the number of '0' characters in the string a up to that point and y is the number of '1' characters in the string a up to that point, stdin is empty.
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
        
    #State: n is an integer between 3 and 3*10^5, a is a string of length n consisting only of 0 and 1, S is a list containing n+1 lists: the first list contains two elements: 0 and 0, the rest of the lists contain two elements: x and y where x is the number of '0' characters in the string a up to that point and y is the number of '1' characters in the string a up to that point, ans is the index i that minimizes the absolute difference between n/2 and i, satisfy is 0, stdin is empty, i is n-1, left is the number of '0' characters in the string a up to the current point i, lsum is the total number of characters in the string a up to the current point i, right is the number of '1' characters in the string a from the current point i to the end, rsum is the total number of characters in the string a from the current point i to the end.
    print(ans)
    #This is printed: n-1 (where n is an integer between 3 and 3*10^5)

#Overall this is what the function does:This function reads two inputs from the standard input: an integer n and a string a of length n consisting only of 0 and 1. It then calculates the cumulative count of 0s and 1s in the string a and stores it in a list S. The function then iterates through the list S to find the index i that minimizes the absolute difference between n/2 and i, while ensuring that the number of 0s and 1s on both sides of the index i are roughly balanced. Finally, the function prints the index i that satisfies these conditions.

#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then a sequence of test cases. Each test case consists of two inputs: first an integer (the number of houses) and then a string of 0s and 1s (the preferences of the residents).
    for _ in range(int(input())):
        func_1()
        
    #State: The function `func_1()` has been executed for the number of test cases specified in the initial state, and its return value is returned. `stdin` is empty.

#Overall this is what the function does:Executes a specified number of test cases, each consisting of a sequence of house preferences, and returns the result of processing these test cases, leaving the standard input empty.

