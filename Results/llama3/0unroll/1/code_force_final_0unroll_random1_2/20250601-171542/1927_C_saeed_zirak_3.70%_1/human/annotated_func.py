#State of the program right berfore the function call: stdin contains an integer t, followed by t test cases. Each test case contains three integers n, m, and k, followed by n integers a_1, a_2, ..., a_n, and m integers b_1, b_2, ..., b_m. 1 <= t <= 10^4, 1 <= n, m <= 2*10^5, 2 <= k <= 2*min(n, m), k is even, 1 <= a_i, b_j <= 10^6.
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
        
    #State: The output state will contain 'yes' or 'no' for each test case, indicating whether it is possible to make the number of ones in both arrays equal to k/2 by swapping elements between the arrays, or not.

#Overall this is what the function does:Determines whether it is possible to make the number of ones in both input arrays equal to k/2 by swapping elements between the arrays, and outputs 'yes' or 'no' for each test case accordingly.

