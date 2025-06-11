#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two positive integers n and m, where 1 <= n, m <= 2 * 10^6. The sum of n and the sum of m over all test cases do not exceed 2 * 10^6.
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        
        count = 2
        
        ans = n
        
        while count <= m:
            countmins = count - 1
            g = n / count
            if g < countmins:
                break
            g -= countmins
            ans += g / count + 1
            count += 1
        
        print(int(ans))
        
    #State: Output State: The output state after the loop executes all the iterations is a series of printed values, each representing the calculated value of `ans` for each test case. The value of `t` remains unchanged, and the values of `n` and `m` for each test case are consumed by the loop and do not persist after the loop finishes. The loop iterates `t` times, and in each iteration, it calculates and prints the value of `ans` based on the values of `n` and `m` for that test case.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of two positive integers n and m. It calculates and prints the value of `ans` for each test case, which represents the result of a series of calculations involving n and m. The function iterates over all test cases, consuming the input values of n and m, and produces a series of printed values, each representing the calculated `ans` for a test case.

