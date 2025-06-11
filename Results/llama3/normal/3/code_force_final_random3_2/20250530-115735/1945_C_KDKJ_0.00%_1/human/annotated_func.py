#State of the program right berfore the function call: stdin contains two inputs: first an integer and then a string of '0' and '1' characters. The integer is a positive integer and is the length of the string.
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
        
    #State: n is a positive integer, a is a string of '0' and '1' characters of length n, S is a list containing n+1 lists, where the first list is [0, 0], and each subsequent list is updated based on the corresponding character in a, stdin is empty.
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
        
    #State: n is a positive integer greater than 0, a is a string of '0' and '1' characters of length n, S is a list containing n+1 lists, where the first list is [0, 0], and each subsequent list is updated based on the corresponding character in a, left is S[i][0], lsum is S[i][0] + S[i][1], right is S[-1][1] - S[i][1], rsum is n - lsum, ans is the index i for which the absolute difference between n/2 and i is minimized, satisfy is 0, i is n, stdin is empty.
    print(ans)
    #This is printed: the integer closest to n/2

#Overall this is what the function does:This function reads an integer and a string of '0' and '1' characters from standard input, where the integer represents the length of the string. It then processes the string to find the index that is closest to the middle of the string, considering the balance of '0's and '1's on both sides of the index. The function prints the index that minimizes the absolute difference between the middle of the string and the index, effectively finding the most balanced point in the string.

#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer and then a string of 0 and 1. The integer is a positive integer and represents the length of the string.
    for _ in range(int(input())):
        func_1()
        
    #State: The function `func_1()` has been executed, `_` is equal to the number of test cases, and stdin contains multiple test cases.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer and a string of 0s and 1s. It then executes the `func_1()` function for each test case, without modifying the input or producing any output. The function's purpose is to process the test cases by executing `func_1()` for each one, without altering the state of the program or the input variables.

