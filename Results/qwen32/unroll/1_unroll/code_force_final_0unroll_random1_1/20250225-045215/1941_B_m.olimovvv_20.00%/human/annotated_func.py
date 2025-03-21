#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 3 <= n <= 2 * 10^5, and a is a list of n integers where each element a_j satisfies 0 <= a_j <= 10^9. The sum of all n values across all test cases does not exceed 2 * 10^5.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        b = list(map(int, input().split()))
        
        if b[0] % 2 == 1 and b[1] != b[0] + 2 or b[-1] % 2 == 1 and b[-2] != b[-1] + 2:
            print('NO')
        else:
            print('YES')
        
    #State: a series of 'YES' or 'NO' responses for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of integers. For each test case, it checks if the first or last element of the list is odd and, if so, whether it is followed or preceded by an element that is exactly two more than itself. If either condition fails, it outputs 'NO'; otherwise, it outputs 'YES'.

