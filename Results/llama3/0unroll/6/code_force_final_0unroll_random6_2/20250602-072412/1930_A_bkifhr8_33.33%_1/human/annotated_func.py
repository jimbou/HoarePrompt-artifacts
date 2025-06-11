#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case contains an integer n (1 <= n <= 50) followed by 2n integers a_1,a_2,\ldots,a_{2n} (1 <= a_i <= 10^7).
    t = int(input())
    ans_f = []
    for i in range(t):
        ans = 0
        
        n = int(input())
        
        l = input()
        
        lst = l.split(' ')
        
        for i in range(n * 2):
            if len(lst) != 2:
                ans += min(int(lst[0]), int(lst[1]))
                lst.remove(lst[0 * 2])
                lst.remove(lst[1 * 2])
            else:
                ans += min(int(lst[0]), int(lst[1]))
                break
        
        ans_f.append(ans)
        
    #State: Output State: The variable t is equal to 0, ans_f is a list containing the sum of the minimum pairs of integers from each test case.
    for i in ans_f:
        print(i)
        
    #State: Output State: The variable t is equal to 0, ans_f is a list containing the sum of the minimum pairs of integers from each test case, and the values in ans_f have been printed to the console.

#Overall this is what the function does:The function reads input from stdin, processes it, and prints the results to the console. It accepts a series of test cases, each containing an integer n followed by 2n integers. For each test case, it calculates the sum of the minimum pairs of integers and stores the results in a list. After processing all test cases, it prints the calculated sums to the console.

