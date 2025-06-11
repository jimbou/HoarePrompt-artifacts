#State of the program right berfore the function call: stdin contains multiple inputs: first an integer (the number of test cases), then for each test case, first an integer (the length of the array), then a list of integers (the elements of the array). The length of the array is between 1 and 200,000 (inclusive), and the sum of the lengths of all arrays does not exceed 200,000. The array elements are between -n and n (inclusive), where n is the length of the array.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        p = [-1] * n
        
        mex = n
        
        for i in range(n - 1, -1, -1):
            p[i] = mex - a[i]
            mex = min(mex, p[i])
        
        print(*p)
        
    #State: Output State: The output state after the loop executes all the iterations is a list of integers, where each integer represents the minimum value of the array elements that are greater than or equal to the current index. The list is printed in reverse order, with the first element being the minimum value of the array elements that are greater than or equal to the last index, and the last element being the minimum value of the array elements that are greater than or equal to the first index.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer array. For each array, it calculates and prints a list of integers representing the minimum value of the array elements that are greater than or equal to the current index, in reverse order. The function processes all test cases and outputs the results in the specified format.

