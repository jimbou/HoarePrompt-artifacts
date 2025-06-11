#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (the length of the array) and then a space-separated list of integers. The length of the list is equal to the first integer. All integers are between 1 and 10^9.
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
        
    #State: t is equal to 0, n is an integer, a is a sorted list of integers, stdin is empty, res is an integer, mdx is an integer, i is an integer. If n is equal to 1, the number 1 is printed. Otherwise, mdx is n // 2 + n % 2 - 1 and mdx must be less than n, i is n. If a[mdx] is equal to a[i] for all i in the range [mdx, n), then res is equal to the number of occurrences of a[mdx] in the range [mdx, n), otherwise res is less than the number of occurrences of a[mdx] in the range [mdx, n), and the value of res is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer (the length of the array) followed by a space-separated list of integers. It sorts the list of integers and then counts the number of occurrences of the middle element (or the element just after the middle if the length is even) in the second half of the list. If the list has only one element, it prints 1. Otherwise, it prints the count of the middle element's occurrences in the second half of the list. The function processes all test cases and prints the results accordingly.

