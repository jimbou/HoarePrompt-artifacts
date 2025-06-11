#State of the program right berfore the function call: stdin contains two inputs: first an integer and then a string consisting only of 0 and 1. The integer is a positive integer greater than or equal to 3.
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
        
    #State: Output State: The value of variable 'S' is a list containing n+1 lists, each containing two elements: the count of 0's and 1's encountered in the string 'a' up to that point, respectively. The value of variable 'a' is unchanged. The value of variable 'n' is unchanged. The stdin is empty.
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
        
    #State: Output State: The value of variable 'S' is a list containing n+1 lists, each containing two elements: the count of 0's and 1's encountered in the string 'a' up to that point, respectively. The value of variable 'a' is unchanged. The value of variable 'n' is unchanged. The value of variable 'ans' is the index 'i' where the condition 'abs(n / 2 - i) <= abs(n / 2 - ans)' is satisfied and either 'left * 2 >= lsum' and 'right * 2 >= rsum' or 'left * 2 < lsum' and 'right * 2 < rsum'. The value of variable 'satisfy' is unchanged. Stdin is empty.
    print(ans)
    #This is printed: the index 'i' where the condition 'abs(n / 2 - i) <= abs(n / 2 - ans)' is satisfied and either 'left * 2 >= lsum' and 'right * 2 >= rsum' or 'left * 2 < lsum' and 'right * 2 < rsum'

#Overall this is what the function does:The function reads an integer and a string of 0s and 1s from standard input, calculates the cumulative counts of 0s and 1s in the string, and then finds the index where the absolute difference between the middle of the string and the current index is minimized, considering the balance of 0s and 1s on both sides of the index. It prints the index that satisfies this condition.

#State of the program right berfore the function call: stdin contains an integer representing the number of test cases, followed by a series of test cases. Each test case consists of an integer n representing the number of houses, followed by a string a of length n consisting only of 0 and 1.
    for _ in range(int(input())):
        func_1()
        
    #State: stdin contains an empty string.

#Overall this is what the function does:Reads a series of test cases from standard input, where each test case consists of an integer representing the number of houses and a string of 0s and 1s, and processes each test case without producing any output or modifying the input, leaving the standard input empty after all test cases have been processed.

