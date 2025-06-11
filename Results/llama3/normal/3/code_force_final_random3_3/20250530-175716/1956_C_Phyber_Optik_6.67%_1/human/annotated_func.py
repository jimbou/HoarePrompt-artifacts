#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains the number of test cases t (1 <= t <= 500). Each test case contains a single integer n (1 <= n <= 500) — the size of the matrix a.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        sum, r = 0, 0
        
        for i in range(1, n + 1):
            if n * (n + 1) // 2 > i * n:
                r = i
                sum += n * (n + 1) // 2
            else:
                sum += i * n
        
        print(sum, n + r)
        
        for j in range(1, n + r + 1):
            if j <= n:
                print(1, j, end=' ')
                print(*range(1, n + 1))
            else:
                print(2, j % n, end=' ')
                print(*range(1, n + 1))
        
    #State: t is an integer greater than or equal to 0, _ is t, n is an integer that must be at least 1, sum is either greater than or equal to n times the sum of n and 1 divided by 2 or equal to n times the sum of n and 1 divided by 2 plus the sum of all integers from 1 to n, r is either n, n - 1, n - 2, ..., 0, i is n, j is n + r, stdin contains -t inputs. If j is less than or equal to n, then "1, j" is printed, followed by a sequence of numbers from 1 to n (inclusive). If j is greater than n, then "2, j % n" is printed, followed by the numbers from 1 to n.

#Overall this is what the function does:This function reads a number of test cases from standard input, then for each test case, it reads an integer n and calculates a sum based on the value of n. It then prints the calculated sum and a sequence of numbers for each test case. The sequence of numbers consists of either "1, j" followed by numbers from 1 to n (inclusive) if j is less than or equal to n, or "2, j % n" followed by numbers from 1 to n if j is greater than n. The function repeats this process for each test case.

