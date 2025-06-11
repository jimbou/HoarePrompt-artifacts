#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains the number of test cases t (1 <= t <= 10^4). Each test case contains two positive integers n and m (1 <= n, m <= 2 * 10^6).
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
        
    #State: The final state after the loop executes all the iterations is that the variable 't' remains unchanged, 'n' and 'm' are updated to the last test case values, 'count' is reset to 2, 'ans' is updated to the result of the last test case, and the standard input 'stdin' is exhausted.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of two positive integers n and m. It calculates and prints the result of a mathematical operation involving n and m for each test case, updating the result based on a conditional loop that increments a counter and modifies the result until a certain condition is met or the counter exceeds m. The function exhausts the standard input and leaves the variables in their final state after processing all test cases.

