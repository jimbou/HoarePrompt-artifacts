#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of an integer n (1 <= n <= 50) followed by 2n integers a_1, a_2, ..., a_2n (1 <= a_i <= 10^7).
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
        
    #State: `t` is at least `n * 2 + t`, `i` is `n * 2 + t - 1`, `ans_f` is a list containing `ans` at least the sum of the minimum of the first two elements of `lst` in each iteration plus the current `ans` value plus the last calculated `ans` value, ..., plus the last calculated `ans` value, `n` is an integer equal to the input value, `l` is a string equal to the input value, `lst` is an empty list, and stdin contains `t-t` inputs: `t-t` test cases.
    for i in ans_f:
        print(i)
        
    #State: `t` is at least `n * 2 + t`, `i` is the last element in `ans_f`, `ans_f` is a list containing all elements, `n` is an integer equal to the input value, `l` is a string equal to the input value, `lst` is an empty list, and stdin contains `t-t` inputs: `t-t` test cases, and the last element in `ans_f` which is `i` is being printed

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n followed by 2n integers. It calculates the sum of the minimum of each pair of integers in each test case and stores these sums in a list. Finally, it prints each sum in the list.

