#State of the program right berfore the function call: stdin contains multiple inputs: first an integer t (1 <= t <= 10^4), then for each test case, first an integer n (3 <= n <= 2 * 10^5), then n integers a_1, a_2, ..., a_n (0 <= a_j <= 10^9).
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
        
    #State: numTest is an integer t (1 <= t <= 10^4) and is equal to 0, n is an integer (3 <= n <= 2 * 10^5), a is a list of n integers where a[i] is reduced by its original value, a[i + 1] is reduced by 3 times the original value of a[i], and a[i + 2] is reduced by the original value of a[i] for all i in the range 0 to n - 2, i is n - 1, and 'NO' or 'YES' is printed for each test case.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It then attempts to reduce the integers in each test case to zero by iteratively subtracting the value of each integer from itself, the next integer, and the integer after that. If it is possible to reduce all integers to zero, it prints 'YES'; otherwise, it prints 'NO'. The function processes multiple test cases and prints the result for each case.

