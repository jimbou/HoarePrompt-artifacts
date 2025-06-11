#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two positive integers n and m, such that 1 <= n, m <= 2 * 10^6.
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
        
    #State: The number of test cases t has been reduced to 0, and the values of n and m have been updated to the values of the last test case. The variable count has been reset to 2, and the variable ans has been updated to the result of the last test case. The loop has printed the results of all test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two positive integers n and m. It calculates and prints the result of a mathematical operation involving n and m for each test case. The function iteratively updates the result based on a conditional logic involving the values of n, m, and a counter variable. Once all test cases have been processed, the function concludes, leaving the input variables updated to their last test case values.

