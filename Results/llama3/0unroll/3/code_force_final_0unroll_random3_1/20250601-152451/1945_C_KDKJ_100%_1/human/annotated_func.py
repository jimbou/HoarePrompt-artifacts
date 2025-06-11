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
        
    #State: n is an integer (unchanged), a is a string '101', S is a list [[0, 0], [0, 1], [1, 1], [1, 2]].
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
        
    #State: To determine the output state after the loop has executed all its iterations, we need to analyze the loop's behavior based on the given initial state.
    #
    #Given:
    #- `n` is an integer
    #- `a` is a string '101'
    #- `S` is a list [[0, 0], [0, 1], [1, 1], [1, 2]]
    #- `ans` is -1
    #
    #The loop iterates from `i = 0` to `n` (inclusive), and its body performs the following operations:
    #
    #1. It calculates `left`, `lsum`, `right`, and `rsum` based on the current value of `i` and the elements of list `S`.
    #2. It checks two conditions:
    #   - If `left * 2 < lsum` or `right * 2 < rsum`, it skips to the next iteration.
    #   - If `abs(n / 2 - i) < abs(n / 2 - ans)`, it updates `ans` to the current value of `i`.
    #
    #To determine the output state, we need to know the value of `n`. However, since `n` is not specified, we will analyze the loop's behavior for a general case.
    #
    #Assuming `n` is a positive integer, the loop will iterate `n + 1` times. The value of `ans` will be updated whenever the condition `abs(n / 2 - i) < abs(n / 2 - ans)` is true.
    #
    #Since `ans` is initially -1, it will be updated to 0 in the first iteration (if `n` is even) or to the value of `i` that minimizes `abs(n / 2 - i)` (if `n` is odd).
    #
    #After the loop finishes executing, the output state will be:
    #
    #Output State: `n` is still an integer, `a` is still a string '101', `S` is still a list [[0, 0], [0, 1], [1, 1], [1, 2]], and `ans` is the value of `i` that minimizes `abs(n / 2 - i)`.
    #
    #In natural language, the output state is that the variables `n`, `a`, and `S` remain unchanged, while the variable `ans` is updated to the value of `i` that is closest to `n / 2`.
    print(ans)
    #This is printed: the integer closest to n / 2

#Overall this is what the function does:This function takes a positive integer n greater than or equal to 3 and a string a of length n consisting only of '0' and '1' as input. It calculates the cumulative sum of '0's and '1's in the string and then finds the index i that minimizes the absolute difference between n/2 and i, considering the constraints that the cumulative sum of '0's up to i is at least half of the total '0's and the cumulative sum of '1's from i to the end is at least half of the total '1's. The function returns the index i that satisfies these conditions and is closest to n/2.

#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer and then a string of length equal to the integer. The string consists only of 0 and 1.
    for _ in range(int(input())):
        func_1()
        
    #State: stdin is empty.

#Overall this is what the function does:Reads multiple test cases from standard input, where each test case consists of an integer and a string of 0s and 1s of equal length, and processes each test case using the func_1 function, leaving the standard input empty after all test cases have been processed.

