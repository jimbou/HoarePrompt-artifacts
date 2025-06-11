#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of three integers n, m, and k (1 <= n, m <= 2*10^5, 2 <= k <= 2*min(n, m), k is even) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^6) and m integers b_1, b_2, ..., b_m (1 <= b_j <= 10^6).
    for t in range(int(input())):
        n, m, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        b = list(map(int, input().split()))
        
        aOnes = 0
        
        bOnes = 0
        
        newk = k // 2
        
        i = 1
        
        while i <= k:
            if i in a and i in b:
                if aOnes < bOnes:
                    aOnes += 1
                else:
                    bOnes += 1
            elif i in a and aOnes <= newk:
                aOnes += 1
            elif i in b and bOnes <= newk:
                bOnes += 1
            else:
                break
            i += 1
        
        if aOnes == newk and bOnes == newk:
            print('yes')
        else:
            print('no')
        
    #State: The output state after the loop executes all the iterations will be a series of 'yes' or 'no' printed to the console, depending on whether the conditions for aOnes and bOnes are met for each test case. The input state remains unchanged, with the same values for t, n, m, k, a, and b.

#Overall this is what the function does:This function reads input from the standard input, processes it according to specific rules, and prints 'yes' or 'no' to the console for each test case. It does not modify the input state. The function iterates over a series of test cases, each consisting of three integers (n, m, k) and two lists of integers (a and b). It then checks if it is possible to increment the count of ones in both lists to a target value (k/2) by iterating over the range from 1 to k and updating the counts based on the presence of the current number in both lists or in one of them. If the target count is reached for both lists, it prints 'yes'; otherwise, it prints 'no'.

