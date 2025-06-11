#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 5000) followed by t test cases. Each test case consists of an integer n (1 ≤ n ≤ 50) followed by 2n integers a_1,a_2,...,a_{2n} (1 ≤ a_i ≤ 10^7).
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
        
    #State: t is 0, ans_f is a list containing t elements where each element is at least the minimum of the first two elements of the original lst, i is n * 2, n is an integer between 1 and 50, lst is an empty list, stdin is empty.
    for i in ans_f:
        print(i)
        
    #State: `t` is 0, `ans_f` is a list containing `n * 2` elements where each element is at least the minimum of the first two elements of the original `lst`, `i` is the last element in the list, `n` is an integer between 1 and 50, `lst` is an empty list, `stdin` is empty, and the last element of the list which is `i` has been printed

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n followed by 2n integers. It then calculates the sum of the minimum values of each pair of integers in each test case and stores these sums in a list. Finally, it prints out the sums for each test case.

