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
        
    #State: The loop will have executed 't' number of times, where 't' is an integer between 1 and 500. For each execution, it will have printed the sum of the series and the value of 'n + r', where 'n' is the input number and 'r' is the largest number such that n*(n+1)//2 > i*n. It will also have printed 'n + r' lines, each containing 'n' numbers. The first 'n' lines will contain the numbers from 1 to 'n', and the remaining lines will contain the numbers from 1 to 'n' in a cyclic manner. The value of 't' will remain unchanged.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a single integer 'n' representing the size of a matrix. For each test case, it calculates the sum of a series based on 'n' and prints the sum along with the value of 'n + r', where 'r' is the largest number such that n*(n+1)//2 > i*n. Additionally, it prints 'n + r' lines, each containing 'n' numbers, with the first 'n' lines containing numbers from 1 to 'n' and the remaining lines containing numbers from 1 to 'n' in a cyclic manner. The function repeats this process for 't' number of test cases, where 't' is an integer between 1 and 500 provided at the beginning of the input.

