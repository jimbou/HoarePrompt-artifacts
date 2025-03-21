#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (2 ≤ n ≤ 100) representing the length of the array a. The next line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the elements of the array a. The number of test cases t (1 ≤ t ≤ 500) is given at the beginning of the input.
def func():
    ntest = int(input())
    for itest in range(0, ntest, 1):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        print(a[len(a) - 1] - a[0])
        
    #State: After executing all iterations, the variables `itest`, `n`, and `a` will have the values from the last test case processed by the loop. The variable `ntest` will remain unchanged as it represents the total number of test cases.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an array of integers. For each test case, it calculates and prints the difference between the maximum and minimum values in the array.

