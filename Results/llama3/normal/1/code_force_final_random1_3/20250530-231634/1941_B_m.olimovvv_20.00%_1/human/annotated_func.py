#State of the program right berfore the function call: stdin contains multiple inputs: first an integer t (1 <= t <= 10^4), then for each test case, first an integer n (3 <= n <= 2 * 10^5), then n integers a_1, a_2, ..., a_n (0 <= a_j <= 10^9).
    for _ in range(int(input())):
        a = int(input())
        
        b = list(map(int, input().split()))
        
        if b[0] % 2 == 1 and b[1] != b[0] + 2 or b[-1] % 2 == 1 and b[-2] != b[-1] + 2:
            print('NO')
        else:
            print('YES')
        
    #State: a is an integer, b is a list of integers, stdin is empty. If the first element of b is odd and the second element is not the first element plus 2, or the last element of b is odd and the second last element is not the last element plus 2, then 'NO' is printed. Otherwise, 'YES' is printed.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and determines whether a given list of integers meets certain conditions. It checks if the first and last elements of the list are odd and if the adjacent elements are not consecutive odd numbers. Based on this, it prints 'YES' if the conditions are met and 'NO' otherwise. The function processes all test cases and empties the stdin.

