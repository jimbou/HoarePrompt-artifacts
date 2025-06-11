#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (the length of the array) and then a list of integers (the array). The length of the array is a non-negative integer and the integers in the array are between 1 and 10^9.
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
        
    #State: t = 0, n = None, a = None, res = None, mdx = None, i = None.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer (array length) followed by a list of integers. It sorts each array and then counts the occurrences of the middle element (or the element just after the middle if the length is even) in the sorted array. The function prints the count of these middle elements for each test case.

