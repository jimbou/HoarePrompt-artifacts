#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 <= n <= 10^5) and then a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
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
        
    #State: t is 0, n is an integer greater than or equal to 1, a is a sorted list of integers between 1 and 10^9 inclusive, stdin contains 0 inputs. If n is 1, the number 1 is printed. Otherwise, res is equal to the number of times a[mdx] appears in a from index mdx to n-1, mdx is an integer equal to n // 2 + n % 2 - 1, and the value of res is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by a list of n integers. It sorts the list of integers and then prints the number of times the middle element (or the element just after the middle if n is even) appears in the sorted list from the middle index to the end. If the list contains only one element, it prints 1. The function continues to process test cases until all input has been read.

