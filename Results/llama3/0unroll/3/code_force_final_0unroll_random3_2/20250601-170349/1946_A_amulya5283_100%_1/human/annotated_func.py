#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (n) and then a list of n integers. n is a positive integer and does not exceed 10^5. The integers in the list are positive and do not exceed 10^9.
    t = int(input())
    while t > 0:
        t -= 1
        
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        if n == 1:
            print(1)
        else:
            res = 0
            mdx = n // 2 + n % 2 - 1
            for i in range(mdx, n):
                if a[mdx] == a[i]:
                    res += 1
            print(res)
        
    #State: The output state is the number of occurrences of the median element in the sorted list for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a positive integer n and a list of n positive integers. It sorts the list and prints the number of occurrences of the median element for each test case. If the list contains only one element, it prints 1. The function processes all test cases and outputs the results in the same order they were input.

