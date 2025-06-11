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
        
    #State: Output State: The variable ans_f is a list containing t integers, each representing the minimum sum of pairs of integers from the input test cases. The variable t is still an integer between 1 and 5000, and stdin is empty since all inputs have been consumed by the loop.
    for i in ans_f:
        print(i)
        
    #State: Output State: The variable ans_f is still a list containing t integers, each representing the minimum sum of pairs of integers from the input test cases. The variable t is still an integer between 1 and 5000, and stdin is empty since all inputs have been consumed by the loop. The loop has printed each integer in ans_f to the console, but the values of ans_f and t remain unchanged.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output to the console. It accepts a series of test cases, each containing an integer n followed by 2n integers. The function calculates the minimum sum of pairs of integers for each test case and stores the results in a list. Finally, it prints each result to the console. The function does not modify the input variables, and its output is a series of integers representing the minimum sum of pairs for each test case.

