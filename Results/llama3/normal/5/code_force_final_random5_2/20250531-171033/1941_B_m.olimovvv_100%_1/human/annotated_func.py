#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n (3 <= n <= 2 * 10^5) and then a list of n integers a_1, a_2, ..., a_n (0 <= a_j <= 10^9). The sum of the values of n over all test cases does not exceed 2 * 10^5.
    for _ in range(int(input())):
        a = int(input())
        
        b = list(map(int, input().split()))
        
        for i in range(0, a - 2):
            if b[i] < 0:
                print('NO')
                break
            b[i + 1] -= b[i] * 2
            b[i + 2] -= b[i]
            b[i] -= b[i]
        else:
            if b[-1] != 0 or b[-2] != 0:
                print('NO')
            else:
                print('YES')
        
    #State: a is an integer that must be at least 3, b is a list of integers where the element at index i+1 is decreased by twice the value of the element at index i, the element at index i+2 is decreased by the value of the element at index i, and the element at index i is set to 0, _ is 0, i is a - 2, stdin contains 0 inputs.

#Overall this is what the function does:Determines whether a given list of integers can be reduced to zero by iteratively subtracting twice the current element from the next element and the current element from the element after next, starting from the first element, and prints 'YES' if possible, 'NO' otherwise.

