#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains an integer n (1 <= n <= 2 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= n) — the integers on the cards in your hand. It is guaranteed that each integer from 1 through n appears in the sequence a_1, a_2, ..., a_n at most 2 times. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: The loop has executed all iterations, and the output state is the final state of the variables after the last iteration. The variable 'ans' holds the total count of pairs of identical integers in all test cases, and the variable 'cnt' holds the count of each integer in the last test case. The input buffer is empty, and the loop variables '_', 'n', 'a', and 'x' hold the values from the last iteration.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a list of n integers. It counts the occurrences of each integer in the list and calculates the total number of pairs of identical integers across all test cases. The function then prints the total count of pairs.

