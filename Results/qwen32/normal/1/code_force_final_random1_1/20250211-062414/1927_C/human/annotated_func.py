#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are integers such that 1 ≤ n, m ≤ 2·10^5, and k is an even integer such that 2 ≤ k ≤ 2 · min(n, m). a is a list of n integers where each element a_i satisfies 1 ≤ a_i ≤ 10^6. b is a list of m integers where each element b_j satisfies 1 ≤ b_j ≤ 10^6. The sum of all n and m across all test cases does not exceed 4 · 10^5.
def func():
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
        
    #State: A series of "yes" or "no" responses for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two lists of integers and an even integer. For each test case, it determines whether it's possible to select exactly half of the value of `k` integers from each list such that the selected integers are common between the two lists or unique to each list without exceeding the count specified by `k`. It outputs "yes" if such a selection is possible for a test case, otherwise "no".

