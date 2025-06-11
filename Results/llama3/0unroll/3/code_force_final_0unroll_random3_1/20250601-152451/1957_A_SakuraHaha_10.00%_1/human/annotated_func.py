#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t test cases. Each test case consists of an integer n (1 <= n <= 100) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 100).
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = dict()
    for x in a:
        cnt[x] = cnt.get(x, 0) + 1
        
    #State: Output State: stdin contains t-1 test cases. Each test case consists of an integer n (1 <= n <= 100) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 100). n is an integer equal to the value of the first test case, a is a list of integers equal to the values of the first test case, ans is 0, cnt is a dictionary where the keys are the unique elements in a and the values are their respective counts.
    for x in cnt.values():
        ans += x // 4
        
    #State: Output State: The value of ans is the sum of the integer division of each count in cnt by 4, while the values of t, n, a, and cnt remain unchanged.
    print(ans)
    #This is printed: sum of the integer division of each count in cnt by 4

#Overall this is what the function does:This function reads an integer n from standard input, followed by n integers, and calculates the sum of the integer division of each unique integer's count by 4. It then prints this sum. The function does not modify the input values or store any results beyond printing the calculated sum.

