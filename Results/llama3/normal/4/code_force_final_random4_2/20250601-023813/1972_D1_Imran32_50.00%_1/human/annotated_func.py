#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains the number of test cases t (1 <= t <= 10^4). Each test case contains two positive integers n, m (1 <= n, m <= 2 * 10^6).
    n, k = map(int, input().split())
    ans = n
    root = int(math.sqrt(n)) + 1
    for i in range(2, root + 1):
        cnt = i * i
        
        ans += (n + i) // cnt
        
    #State: n is a positive integer, k is a positive integer, ans is equal to n plus the sum of (n + i) divided by i squared rounded down for i from 2 to the square root of n rounded up to the nearest integer, root is an integer equal to the square root of n rounded up to the nearest integer, stdin contains one less test case, i is equal to the square root of n rounded up to the nearest integer plus 1.
    print(ans)
    #This is printed: ans (where ans is a positive integer equal to n plus the sum of (n + i) divided by i squared rounded down for i from 2 to the square root of n rounded up to the nearest integer)

#Overall this is what the function does:This function reads a test case from standard input, where the test case consists of two positive integers n and k. It calculates a value 'ans' by adding to n the sum of the integer divisions of (n + i) by i squared, where i ranges from 2 to the square root of n rounded up to the nearest integer. The function then prints the calculated 'ans' value. The function does not modify the input variables n and k, and it does not perform any actions other than reading input and printing output. The function's purpose is to compute and display a specific mathematical expression based on the input values n and k.

