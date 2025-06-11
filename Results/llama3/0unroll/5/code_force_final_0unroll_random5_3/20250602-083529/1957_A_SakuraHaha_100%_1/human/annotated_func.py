#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two lines of input. The first line contains an integer n (1 ≤ n ≤ 100). The second line contains n integers a_1, a_2, …, a_n (1 ≤ a_i ≤ 100).
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = dict()
    for x in a:
        cnt[x] = cnt.get(x, 0) + 1
        
    #State: Output State: cnt is a dictionary where the keys are the unique integers in list a and the values are their respective counts, ans is 0, n is an integer between 1 and 100, a is a list of n integers between 1 and 100, stdin contains t-1 test cases.
    for x in cnt.values():
        ans += x // 3
        
    #State: Output State: The value of ans is the sum of the integer divisions of the values in cnt by 3, cnt is a dictionary where the keys are the unique integers in list a and the values are their respective counts, n is an integer between 1 and 100, a is a list of n integers between 1 and 100, stdin contains t-1 test cases.
    print(ans)
    #This is printed: sum of the integer divisions of the counts of unique integers in list a by 3

#Overall this is what the function does:This function reads a test case from standard input, where the test case consists of an integer n followed by n integers. It counts the occurrences of each unique integer, calculates the sum of the integer divisions of these counts by 3, and prints this sum. The function does not modify the input values and does not have any side effects other than printing the result.

