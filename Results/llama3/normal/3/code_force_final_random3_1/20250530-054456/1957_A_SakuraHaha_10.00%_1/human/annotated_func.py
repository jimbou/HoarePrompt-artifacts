#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two lines. The first line contains an integer n (1 <= n <= 100). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 100).
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = dict()
    for x in a:
        cnt[x] = cnt.get(x, 0) + 1
        
    #State: n is an integer between 1 and 100, a is a list of n integers between 1 and 100, ans is 0, cnt is a dictionary with x as a key and its value is the count of x in the list a plus n, stdin contains t-1 test cases, x is the nth integer in the list
    for x in cnt.values():
        ans += x // 4
        
    #State: n is an integer between 1 and 100, a is a list of n integers between 1 and 100, ans is increased by the integer division of all values in cnt by 4, cnt is a dictionary with all values, stdin contains t-1 test cases, x is the last value in the cnt dictionary
    print(ans)
    #This is printed: ans (where ans is the sum of the integer division of all values in cnt by 4)

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the sum of the integer division of the count of each integer in the input by 4. It accepts no parameters and returns no value, only printing the result to stdout. The function processes one test case at a time, where each test case consists of an integer n followed by n integers. The function counts the occurrences of each integer, calculates the sum of the integer division of these counts by 4, and prints this sum. The function repeats this process for all test cases provided in the input.

