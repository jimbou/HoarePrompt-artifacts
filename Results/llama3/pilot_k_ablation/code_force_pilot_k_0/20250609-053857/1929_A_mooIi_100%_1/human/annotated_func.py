#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (n) and then a list of n integers. n is an integer such that 2 <= n <= 100. The integers in the list are such that 1 <= a_i <= 10^9.
    for _ in range(int(input())):
        n = int(input())
        
        ar = list(sorted(list(map(int, input().split()))))
        
        print(sum([(ar[i] - ar[i - 1]) for i in range(1, n)]))
        
    #State: The sum of the differences between consecutive elements in each sorted list of integers, for all test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by a list of n integers. It sorts each list of integers and calculates the sum of the differences between consecutive elements in the sorted list. The function then prints the calculated sum for each test case.

