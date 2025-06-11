#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of two lines. The first line contains three integers n, f, and k (1 <= f, k <= n <= 100). The second line contains n integers a_i (1 <= a_i <= 100).
    t = int(input())
    for _ in range(t):
        n, f, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        favorite_value = a[f - 1]
        
        same_value_count = 0
        
        for value in a:
            if value == favorite_value:
                same_value_count += 1
        
        greater_count = 0
        
        for value in a:
            if value > favorite_value:
                greater_count += 1
        
        if greater_count >= k:
            print('YES')
        elif greater_count + same_value_count <= k:
            print('NO')
        else:
            print('MAYBE')
        
    #State: The output state will contain t lines, each with either 'YES', 'NO', or 'MAYBE', depending on the values of n, f, k, and the list a in each test case. The value of t remains unchanged.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and outputs 'YES', 'NO', or 'MAYBE' for each case based on the number of values greater than or equal to a favorite value in a list, and the given threshold k. The function takes no parameters and returns no values, but modifies the output state with the results of the test cases.

