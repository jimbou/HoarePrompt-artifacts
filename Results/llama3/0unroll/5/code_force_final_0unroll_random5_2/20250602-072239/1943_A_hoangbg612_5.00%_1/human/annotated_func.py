#State of the program right berfore the function call: stdin contains multiple test cases. The first line of stdin contains a single integer t (1 <= t <= 2 * 10^4) — the number of test cases. For each test case, the first line contains a single integer n (1 <= n <= 2 * 10^5), and the second line contains n integers a_1, a_2, ..., a_n (0 <= a_i < n).
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
        
    #State: The output state is the maximum number of consecutive integers that can be formed from the input list, considering the frequency of each integer. The loop iterates T times, and for each iteration, it reads the size of the list S and the list of integers N. It sorts the list, initializes a dictionary M to store the frequency of each integer, and a variable cur to keep track of the maximum consecutive integer. It then iterates over the sorted list, updating the frequency of each integer in M and updating cur if the current integer is greater than cur. If the sum of the frequencies in M is equal to S, it increments cur. Finally, it iterates from 0 to cur and prints the maximum consecutive integer that can be formed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a list of integers. It determines the maximum number of consecutive integers that can be formed from the input list, considering the frequency of each integer. The function iterates over each test case, sorts the list, and updates the frequency of each integer. It then finds the maximum consecutive integer that can be formed and prints it. The function repeats this process for all test cases.

