#State of the program right berfore the function call: stdin contains multiple test cases. The first line of stdin contains a single integer t (1 ≤ t ≤ 2 * 10^4) — the number of test cases. The description of the test cases follows. The first line of each test case contains a single integer n (1 ≤ n ≤ 2 * 10^5). The second line of each test case contains n integers a_1, a_2, …, a_n (0 ≤ a_i < n).
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        cntl = [(0) for _ in range(n + 1)]
        
        for i in a:
            cntl[i] += 1
        
        if cntl[0] == 0:
            print(0)
        else:
            c = min(2, cntl[0])
            for j in range(1, n + 1):
                if cntl[j] < 2:
                    c -= 1
                    if not c or j == n:
                        print(j)
                        break
        
    #State: n is an integer, a is an empty list, cntl is a list of n+1 elements where each element at index i is equal to the number of occurrences of i in the original list a, stdin contains no test cases, _ is the last integer in the original list a plus the number of test cases, i is the last integer in the original list a. If cntl[0] is 0, then the number 0 is printed. If cntl[0] is not 0, then n is an integer greater than or equal to 0, cntl[0] is not equal to 0, and j is n. If cntl[j] is less than 2, then if c is false or j is equal to n, we break out of the most internal loop or if statement.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a list of integers. It then finds the smallest integer that appears at least twice in the list, or the smallest integer that appears only once if no such integer exists. If the list contains no zeros, it prints 0. The function processes all test cases and prints the result for each case.

