#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing two integers n and k (2 <= n <= 10^8, 1 <= k <= 4n - 2).
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        if k == 1:
            print(1)
            continue
        
        if k <= 2 * n:
            print(math.ceil(k / 2))
        else:
            print(k // 2 + 1)
        
    #State: `n` is an integer between 2 and 10^8 (inclusive), `k` is an integer between 1 and 4n - 2 (inclusive), stdin is empty, int(input()) is 0. If `k` is 1, the number 1 is printed and we move to the next iteration of the loop. Otherwise, if `k` is less than or equal to 2n, the ceiling of k divided by 2 is printed, which is the ceiling of an integer between 1 and 2n - 1 (inclusive) divided by 2. If `k` is greater than 2n, k // 2 + 1 is printed, where k is an integer between 1 and 4n - 2 (inclusive) and n is an integer between 2 and 10^8 (inclusive).

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers, n and k. It then prints the ceiling of k divided by 2 if k is less than or equal to 2n, or k divided by 2 plus 1 if k is greater than 2n. If k is 1, it simply prints 1. The function processes all test cases and then exits, leaving the standard input empty.

