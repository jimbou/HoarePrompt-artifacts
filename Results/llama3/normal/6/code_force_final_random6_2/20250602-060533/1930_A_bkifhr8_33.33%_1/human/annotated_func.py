#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 5000) followed by t test cases. Each test case consists of an integer n (1 ≤ n ≤ 50) followed by 2n integers a_1,a_2,\ldots,a_{2n} (1 ≤ a_i ≤ 10^7).
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
        
    #State: `t` is an integer between 1 and 5000 inclusive, `ans_f` is a list containing the sum of the minimum of the first two elements of `lst` and its original value plus the original value of `ans` and the value of `ans` which is the original value of `ans` plus `n` * 2 times the minimum of the first two elements of `lst` for each iteration, `i` is `t`, `ans` is the original value of `ans` plus `n` * 2 times the minimum of the first two elements of `lst` for each iteration, `l` is a string containing the input string, `n` is an integer, `lst` is an empty list, and stdin contains -t test cases.
    for i in ans_f:
        print(i)
        
    #State: `t` is an integer between 1 and 5000 inclusive, `ans_f` is a list that must have at least `t` elements, `i` is the last element of `ans_f`, `ans` is the original value of `ans` plus `n` * 2 times the minimum of the first two elements of `lst` for each iteration, `l` is a string containing the input string, `n` is an integer, `lst` is a list that must have at least 2 elements, and stdin contains -t test cases, and the value of `i` which is equal to `t` is being printed

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the results. It expects the input to start with an integer t, representing the number of test cases, followed by t test cases. Each test case consists of an integer n, representing the number of pairs, followed by 2n integers. The function calculates the sum of the minimum of each pair of integers for each test case and stores the results in a list. Finally, it prints the results for each test case.

