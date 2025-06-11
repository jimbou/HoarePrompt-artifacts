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
        
    #State: t is 0, _ is t, n is an integer that must be at least 1, sum is n * (n + 1) * (n + 2) // 6, r is n, i is n + 1, j is n + r + 1, stdin contains 0 inputs. If j is less than or equal to n, then "1 [j] " (where [j] is the current value of j which is n + r + 1) and a sequence of numbers from 1 to n (inclusive) are printed. If j is larger than n, then 2, the remainder of j divided by n, and the numbers from 1 to n (inclusive) are printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains a single integer n representing the size of a matrix. For each test case, it calculates the sum of the first n positive integers and the number of rows (r) required to satisfy a certain condition. It then prints the calculated sum and the value of r plus n. Additionally, it prints a sequence of numbers for each row, where the first row contains the numbers 1 to n, and subsequent rows contain the numbers 1 to n, but with an offset of 1 for each row. The function continues this process until all test cases have been processed, at which point the standard input is empty.

