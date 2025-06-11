#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains three integers n, m, and k (1 <= n, m <= 2*10^5, 2 <= k <= 2*min(n, m), k is even) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^6) and m integers b_1, b_2, ..., b_m (1 <= b_j <= 10^6).
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
        
    #State: n, m, k are integers greater than or equal to 1, a is a list of integers, b is a list of integers, newk is k divided by 2, i is k + 1, Stdin is empty. If aOnes is equal to newk and bOnes is equal to newk, then 'yes' is printed. Otherwise, 'no' is printed.

#Overall this is what the function does:This function determines whether it is possible to select k/2 elements from two lists, a and b, such that the selected elements are common to both lists or are present in one of the lists but not the other, and the total count of selected elements in each list is k/2. The function reads input from stdin, processes multiple test cases, and prints 'yes' if the condition is met, otherwise prints 'no'.

