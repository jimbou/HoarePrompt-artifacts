#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 500) followed by t test cases. Each test case contains an integer n (2 ≤ n ≤ 100) followed by n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9).
    ntest = int(input())
    for itest in range(0, ntest, 1):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        kq = 0
        
        for i in range(0, len(a) // 2, 1):
            kq = kq + a[len(a) - i - 1] - a[i]
        
        print(kq)
        
    #State: The loop will execute ntest times, each time reading an integer n and a list of n integers from stdin, sorting the list in ascending order, and printing the sum of the differences between the largest and smallest elements, the second largest and second smallest elements, and so on, until the middle of the list is reached. The value of ntest remains unchanged.

#Overall this is what the function does:Reads a specified number of test cases from standard input, where each test case consists of an integer n followed by n integers. For each test case, it sorts the integers in ascending order and calculates the sum of the differences between the largest and smallest elements, the second largest and second smallest elements, and so on, until the middle of the list is reached. The calculated sum is then printed to standard output.

