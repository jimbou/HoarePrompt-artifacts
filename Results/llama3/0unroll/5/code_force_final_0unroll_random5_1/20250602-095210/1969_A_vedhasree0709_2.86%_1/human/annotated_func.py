#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of an integer n (2 <= n <= 50) followed by n distinct integers p_1, p_2, ..., p_n (1 <= p_i <= n; p_i != i).
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        i = 0
        
        j = 0
        
        while i <= n - 1:
            if l[i] == i + 2 and l[i + 1] == i + 1:
                print(2)
                j = 1
                break
            i += 1
        
        if j == 0:
            print(3)
        
    #State: The output state is a series of integers, each representing the minimum number of swaps required to sort the list of distinct integers. If a pair of adjacent elements is found where the first element is equal to the second index plus 2 and the second element is equal to the first index plus 1, the output is 2. Otherwise, the output is 3. The number of output integers is equal to the input integer t.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a list of distinct integers. It then determines the minimum number of swaps required to sort the list. If a specific condition is met, where a pair of adjacent elements is found in a particular order, the function outputs 2. Otherwise, it outputs 3. The function processes multiple test cases and outputs the minimum number of swaps required for each case.

