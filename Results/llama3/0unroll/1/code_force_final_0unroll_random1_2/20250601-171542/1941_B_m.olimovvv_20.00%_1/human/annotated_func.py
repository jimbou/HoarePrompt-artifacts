#State of the program right berfore the function call: stdin contains multiple inputs: first an integer t (1 <= t <= 10^4), then for each test case, first an integer n (3 <= n <= 2 * 10^5) and then n integers a_1, a_2, ..., a_n (0 <= a_j <= 10^9).
    for _ in range(int(input())):
        a = int(input())
        
        b = list(map(int, input().split()))
        
        if b[0] % 2 == 1 and b[1] != b[0] + 2 or b[-1] % 2 == 1 and b[-2] != b[-1] + 2:
            print('NO')
        else:
            print('YES')
        
    #State: The output state will contain 'YES' or 'NO' for each test case, indicating whether the given conditions are met or not. The number of 'YES' or 'NO' outputs will be equal to the number of test cases (t). The stdin will be empty after the loop executes all the iterations.

#Overall this is what the function does:Evaluates multiple test cases to determine if a given list of integers meets specific conditions, printing 'YES' if the conditions are met and 'NO' otherwise.

