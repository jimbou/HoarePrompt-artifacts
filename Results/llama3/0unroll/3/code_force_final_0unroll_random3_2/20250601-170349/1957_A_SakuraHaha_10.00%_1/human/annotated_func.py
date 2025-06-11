#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two lines. The first line contains an integer n. The second line contains n space-separated integers. t is a positive integer and 1 <= n <= 100. The integers in the second line are positive integers and 1 <= a_i <= 100.
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = dict()
    for x in a:
        cnt[x] = cnt.get(x, 0) + 1
        
    #State: Output State: cnt is a dictionary where the keys are the unique integers in a and the values are their respective counts.
    for x in cnt.values():
        ans += x // 4
        
    #State: Output State: The value of ans is increased by the sum of the integer divisions of the values in cnt by 4.
    print(ans)
    #This is printed: ans (where ans is the value of ans after being increased by the sum of the integer divisions of the values in cnt by 4)

#Overall this is what the function does:This function reads a test case from standard input, where the test case consists of an integer n followed by n space-separated integers. It then counts the occurrences of each unique integer and calculates the sum of the integer divisions of these counts by 4. Finally, it prints the result of this calculation.

