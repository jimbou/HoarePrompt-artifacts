#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains the number of test cases t (1 <= t <= 500). Each test case contains a single integer n (1 <= n <= 500) — the size of the matrix a.
    for _ in range(int(input())):
        n = int(input())
        
        mat = [list(range(1, n + 1)) for i in range(n)]
        
        res = 0
        
        for i in range(n):
            res += (i + 1) * (2 * i + 1)
        
        print(res, n << 1)
        
        for i in range(n, 0, -1):
            print('1 %d' % i, *range(1, n + 1))
            print('2 %d' % i, *range(1, n + 1))
        
    #State: `n` is a positive integer that must be greater than or equal to 1, `i` is 0, `mat` is a 2D list with `n` rows and `n` columns where each row contains numbers from 1 to `n`, `res` is the sum of `(i + 1) * (2 * i + 1)` for `i` from 0 to `n-1`, `_` is equal to the number of test cases, `stdin` is empty, and this is printed: the sum of `(i + 1) * (2 * i + 1)` for `i` from 0 to `n-1` which is equal to `res`, and the number 2 multiplied by `n` which is equal to `n << 1`, and the string '1 %d' % i, and the numbers from 1 to `n` (inclusive) are being printed, and the string '2 %d' % i is printed where `i` is equal to `n`, and the numbers from 1 to `n` (inclusive) are being printed, and the string '1 %d' % i is printed where `i` is equal to `n - 1`, and the numbers from 1 to `n` (inclusive) are being printed, and the string '2 %d' % i is printed where `i` is equal to `n - 1`, and the numbers from 1 to `n` (inclusive) are being printed, and the string '1 %d' % i is printed where `i` is equal to `n - 2`, and the numbers from 1 to `n` (inclusive) are being printed, and the string '2 %d' % i is printed where `i` is equal to `n - 2`, and the numbers from 1 to `n` (inclusive) are being printed, and so on until `i` is equal to 1, and the string '1 %d' % i is printed where `i` is equal to 1, and the numbers from 1 to `n` (inclusive) are being printed, and the string '2 %d' % i is printed where `i` is equal to 1, and the numbers from 1 to `n` (inclusive) are being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains a single integer n representing the size of a matrix. It then calculates the sum of the products of consecutive integers from 1 to n and prints this sum along with twice the value of n. Additionally, it prints a series of strings and numbers in a specific pattern, where the strings are in the format '1 %d' and '2 %d' and the numbers range from 1 to n. The function repeats this process for each test case and does not return any value.

