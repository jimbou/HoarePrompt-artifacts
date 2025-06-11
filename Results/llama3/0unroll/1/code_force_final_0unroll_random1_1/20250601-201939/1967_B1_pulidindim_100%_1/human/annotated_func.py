#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two positive integers n and m (1 <= n, m <= 2 * 10^6).
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        
        count = 2
        
        ans = n
        
        while count <= m:
            countmins = int(count - 1)
            g = int(n / count)
            if g < countmins:
                break
            g -= countmins
            ans += int(g / count) + 1
            count += 1
        
        print(int(ans))
        
    #State: Output State: The loop will execute t times, and for each execution, it will print the value of ans, which is the sum of n and the number of times the while loop runs. The while loop runs as long as count is less than or equal to m and n divided by count is greater than or equal to count minus 1. In each iteration of the while loop, ans is incremented by the integer division of n divided by count minus count minus 1, plus 1. The value of count is incremented by 1 in each iteration. The final value of ans is printed after the while loop finishes. The value of t is not changed by the loop.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two positive integers n and m. For each test case, it calculates and prints the sum of n and the number of times a while loop runs, where the loop runs as long as a certain condition involving n and a counter is met. The counter is incremented by 1 in each iteration, and the sum is updated based on the integer division of n by the counter. The function executes this process for a number of test cases specified by the input, printing the final sum for each test case.

