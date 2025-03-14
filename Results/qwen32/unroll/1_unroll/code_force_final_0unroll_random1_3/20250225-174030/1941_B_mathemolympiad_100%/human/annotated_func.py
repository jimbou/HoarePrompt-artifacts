#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 3 ≤ n ≤ 2 · 10^5, and a is a list of n integers where 0 ≤ a_j ≤ 10^9. The sum of all n across all test cases does not exceed 2 · 10^5.
def func():
    numTest = int(input())
    for _ in range(0, numTest):
        n = int(input())
        
        a = [int(x) for x in input().split()]
        
        stop = False
        
        for i in range(0, n - 2):
            if a[i] < 0:
                print('NO')
                stop = True
                break
            opNum = a[i]
            a[i] -= opNum
            a[i + 1] -= 2 * opNum
            a[i + 2] -= opNum
        
        if stop == True:
            continue
        
        if a[len(a) - 1] != 0 or a[len(a) - 2] != 0:
            print('NO')
        else:
            print('YES')
        
    #State: A sequence of 'YES' or 'NO' for each test case based on the conditions met in the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of integers. For each test case, it checks if the list can be reduced to all zeros by applying a specific operation: subtracting a value from three consecutive elements in the list. If the list can be reduced to all zeros, it prints 'YES'; otherwise, it prints 'NO'.

