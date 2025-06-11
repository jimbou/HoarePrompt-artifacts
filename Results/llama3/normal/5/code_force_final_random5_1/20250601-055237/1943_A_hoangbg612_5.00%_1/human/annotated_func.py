#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (1 <= integer <= 2 * 10^4) and then a list of integers (0 <= integer < 2 * 10^5). The sum of the lengths of the lists over all test cases does not exceed 2 * 10^5.
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
        
    #State: T is 0, S is an integer equal to the first input, N is a list with at least one element, M is a dictionary where the keys are the unique integers from the second input and the values are their respective counts, stdin is empty. If the sum of the counts of all unique integers in M equals S, then cur is the last integer in the sorted list of integers from the second input plus one and i is -1. Otherwise, cur is the smallest integer i such that M[i] is greater than i and i is equal to cur, and cur is printed

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer S and a list of integers N. It sorts the list N, counts the occurrences of each unique integer, and determines the smallest integer i such that the count of i is greater than i. If the sum of the counts of all unique integers equals S, it prints the last integer in the sorted list plus one; otherwise, it prints the smallest integer i that meets the condition. The function processes all test cases and prints the corresponding results.

