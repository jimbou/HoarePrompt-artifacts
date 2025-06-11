#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains a single integer t (1 <= t <= 2 * 10^4). Each test case contains two lines. The first line contains a single integer n (1 <= n <= 2 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (0 <= a_i < n).
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        cntl = [(0) for _ in range(n + 1)]
        
        for i in a:
            cntl[i] += 1
        
        if cntl[0] == 0:
            print(0)
        else:
            c = min(2, cntl[0])
            for j in range(1, n + 1):
                if cntl[j] < 2:
                    c -= 1
                    if not c or j == n:
                        print(j)
                        break
        
    #State: The loop has finished executing all iterations, and the program has terminated. The output state is the final state of the program after all test cases have been processed. The value of n is the last value read from the input, a is an empty list, cntl is a list of n+1 integers where cntl[i] is the count of i in the last list of integers read from the input, and stdin is empty. If cntl[0] is 0, the last output is 0. Otherwise, cntl[0] is not equal to 0, and the last output is the last value of j, which is either the smallest index j such that cntl[j] < 2 or n if no such j exists.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case contains a list of integers. It counts the occurrences of each integer in the list and then finds the smallest index j such that the count of j is less than 2. If no such j exists, it returns the length of the list. If the count of 0 is 0, it returns 0. The function prints the result for each test case and terminates after processing all test cases.

