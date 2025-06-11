#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains the number of test cases t (1 <= t <= 10^4). Each test case contains two positive integers n and m (1 <= n, m <= 2 * 10^6).
    n, k = map(int, input().split())
    ans = n
    root = int(math.sqrt(n)) + 1
    for i in range(2, root + 1):
        cnt = i * i
        
        ans += (n + i) // cnt
        
    #State: n is a positive integer, k is a positive integer, ans is equal to n plus the sum of (n + i) // (i * i) for i from 2 to root, root is an integer equal to the square root of n plus 1, stdin contains one less test case, i is equal to root + 1.
    print(ans)
    #This is printed: n + sum of (n + i) // (i * i) for i from 2 to root (where n is a positive integer, root is the square root of n plus 1, and i is equal to root + 1)

#Overall this is what the function does:The function reads a test case from standard input, where the test case consists of two positive integers n and k. It calculates a value 'ans' by adding n to the sum of (n + i) // (i * i) for i ranging from 2 to the square root of n plus 1. The function then prints the calculated value 'ans'. The function does not modify the input variables n and k, and it does not have any side effects other than printing the result. The function's purpose is to compute and output a specific mathematical expression based on the input values n and k.

