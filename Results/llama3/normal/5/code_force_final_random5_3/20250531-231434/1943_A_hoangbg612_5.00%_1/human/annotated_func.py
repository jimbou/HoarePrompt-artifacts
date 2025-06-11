#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (1 ≤ n ≤ 2 * 10^5). The second line contains n integers a_1, a_2, …, a_n (0 ≤ a_i < n).
    T = int(input())
    for _ in range(T):
        S = int(input())
        
        N = list(map(int, input().split()))
        
        N.sort()
        
        cur = -1
        
        M = {}
        
        for num in N:
            if num > cur:
                if num > cur + 1:
                    cur += 1
                    break
                cur = num
                M[cur] = 1
            else:
                M[cur] += 1
        
        if sum([M[k] for k in M.keys()]) == S:
            cur += 1
        
        for i in range(cur):
            if M[i] <= i:
                cur = i
                break
        
        print(cur)
        
    #State: T is equal to 0, _ is equal to T, S is an integer, N is an empty list, stdin contains no test cases, M is a dictionary with key -1 and value equal to the number of times -1 appears in the original list N, and key equal to each integer i in the original list N that is greater than -1 and value equal to the number of times i appears in the original list N. If the value of M[i] is less than or equal to the value of i, then cur is equal to the smallest integer i such that M[i] is less than or equal to i, otherwise cur is equal to the last element in the original list N plus 1, and cur is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a single integer n followed by n integers. It processes each test case by sorting the integers, counting the occurrences of each integer, and then finding the smallest integer i such that the count of i is less than or equal to i. If no such integer is found, it returns the last integer in the sorted list plus 1. The function prints the result for each test case and consumes all input from standard input.

