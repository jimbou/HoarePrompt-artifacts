#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains three integers t, f, and k (1 <= t, f, k <= 100). The second line contains t integers a_i (1 <= a_i <= 100).
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
        
    #State: The output state is a series of 'YES', 'NO', or 'MAYBE' printed to the console, each corresponding to a test case. The number of outputs is equal to the number of test cases in the input. The value of 't' remains unchanged.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines: the first line contains three integers (t, f, k), and the second line contains t integers. For each test case, it identifies the favorite value (the integer at index f-1), counts the occurrences of this value, and counts the number of integers greater than the favorite value. Based on these counts, it prints 'YES' if the number of greater values is at least k, 'NO' if the sum of the same and greater values is less than or equal to k, and 'MAYBE' otherwise. The function processes all test cases and prints the corresponding results to the console.

