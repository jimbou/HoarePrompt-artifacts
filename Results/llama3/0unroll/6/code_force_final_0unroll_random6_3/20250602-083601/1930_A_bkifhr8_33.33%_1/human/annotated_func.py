#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of an integer n (1 <= n <= 50) followed by 2n integers a_1, a_2, ..., a_{2n} (1 <= a_i <= 10^7).
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
        
    #State: Output State: The variable ans_f is a list of t integers, each representing the minimum sum of pairs of integers in each test case. The variable t is still an integer between 1 and 5000, and stdin is empty since all test cases have been read.
    for i in ans_f:
        print(i)
        
    #State: Output State: The variable ans_f is a list of t integers, each representing the minimum sum of pairs of integers in each test case. The variable t is still an integer between 1 and 5000, and stdin is empty since all test cases have been read. The loop has printed all the elements of ans_f to the console.

#Overall this is what the function does:Reads a series of test cases from standard input, where each test case consists of an integer n followed by 2n integers. For each test case, it calculates the minimum sum of pairs of integers and stores the results in a list. Finally, it prints each result to the console.

