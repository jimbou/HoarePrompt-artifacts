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
        
    #State: n is an integer greater than or equal to 3, a is a string of length n consisting only of 0 and 1, S is a list containing a list with two elements, both 0, and n additional lists with two elements, x and y, where x is the number of 0's in a and y is the number of 1's in a, and stdin is empty.
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
        
    #State: n is an integer greater than or equal to 3, a is a string of length n consisting only of 0 and 1, S is a list containing a list with two elements, both 0, and n additional lists with two elements, x and y, where x is the number of 0's in a and y is the number of 1's in a, stdin is empty, left is the number of 0's in a up to index n, lsum is n, right is the number of 1's in a minus the number of 1's up to index n, rsum is 0, i is n, ans is the value of i that is closest to n/2.
    print(ans)
    #This is printed: the integer closest to n/2

#Overall this is what the function does:This function reads two inputs from stdin: an integer n (n >= 3) and a string a of length n consisting only of 0 and 1. It then calculates the number of 0's and 1's in the string and finds the index i that is closest to n/2, considering the balance between the number of 0's and 1's on the left and right sides of the string. The function prints the value of i that satisfies this condition.

#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer and then a string of 0 and 1. The integer is a positive integer greater than or equal to 3 and less than or equal to 3*10^5. The length of the string is equal to the integer.
    for _ in range(int(input())):
        func_1()
        
    #State: stdin contains no more test cases, the function func_1() has been executed a number of times equal to the number of test cases in the initial state.

#Overall this is what the function does:Executes a function named func_1() for a number of times equal to the number of test cases present in the standard input, where each test case consists of an integer and a string of 0 and 1, without modifying the input or producing any output.

