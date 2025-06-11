#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (greater than 1) and then a list of distinct integers (from 1 to the integer) of the same length as the integer.
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        i = 0
        
        j = 0
        
        while i <= n - 1:
            p = l[i]
            q = l[p - 1]
            if q == i + 1:
                print(2)
                j = 1
                break
            i += 1
        
        if j == 0:
            print(3)
        
    #State: `_` is equal to the number of test cases, `n` is the last integer from stdin, `l` is the last list of integers from stdin, `i` is equal to `n`, `j` is either 0 or 1, `p` is the last element of `l`, `q` is the element of `l` at index `p - 1`. If `j` is 0, the number 3 is being printed. Otherwise, no additional actions are performed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a list of distinct integers from 1 to n. It then checks if the list contains a cycle of length 2 by iterating through the list and checking if the element at index i is equal to i+1. If such a cycle is found, it prints 2 and stops. If no such cycle is found after iterating through the entire list, it prints 3. The function does not modify the input variables and only prints the result to standard output.

