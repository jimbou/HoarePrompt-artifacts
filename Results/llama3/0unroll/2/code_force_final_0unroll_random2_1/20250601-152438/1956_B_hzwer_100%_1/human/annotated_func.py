#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains a single integer n (1 <= n <= 2 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= n) — the integers on the cards in your hand. Each integer from 1 through n appears in the sequence a_1, a_2, ..., a_n at most 2 times. The sum of n over all test cases does not exceed 2 * 10^5.
    input = sys.stdin.readline
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        cnt = [0] * (n + 1)
        
        for x in a:
            cnt[x] += 1
        
        ans = 0
        
        for x in cnt:
            ans += max(0, x - 1)
        
        print(ans)
        
    #State: Output State: The output state after the loop executes all the iterations is that the variable `ans` will hold the total count of pairs of integers in the input sequence `a` for each test case, and this count will be printed to the standard output. The input stream `stdin` will be exhausted, and the variables `n`, `a`, and `cnt` will hold the values from the last test case. The loop variable `_` will be equal to the number of test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a sequence of integers. It counts the number of pairs of identical integers in each sequence and prints the total count of pairs for each test case. The function processes all test cases and exhausts the input stream, leaving the variables from the last test case in memory.

