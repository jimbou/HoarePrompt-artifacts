#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (the size of the array) and then a list of integers (the elements of the array). The size of the array is a positive integer and the elements of the array are positive integers not larger than the size of the array.
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        a, b = float('inf'), float('inf')
        
        c = 0
        
        for x in range(n):
            if a > b:
                a, b = b, a
            if l[x] <= a:
                a = l[x]
            elif l[x] <= b:
                b = l[x]
            else:
                a = l[x]
                c += 1
        
        print(c)
        
    #State: The loop has finished executing, and the final output state is that `n` is an integer greater than or equal to 0, `l` is a list of integers, `a` is the smallest element in `l`, `b` is the second smallest element in `l`, `c` is the number of elements in `l` that are greater than the second smallest element, `x` is `n`, stdin is empty, and the number of elements in `l` that are greater than the second smallest element, which is `c`, has been printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer (array size) and a list of integers (array elements). It then finds the smallest and second smallest elements in the array, and counts the number of elements greater than the second smallest. The function prints the count of such elements for each test case, and continues until all test cases have been processed, leaving the standard input empty.

