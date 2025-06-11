#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (the size of the array) and then a list of integers (the elements of the array). The size of the array is a non-negative integer and the elements of the array are non-negative integers less than or equal to the size of the array.
    for _ in range(int(input())):
        n = int(input())
        
        *inp, = map(int, input().split())
        
        x = y = n + 1
        
        ans = 0
        
        for a in inp:
            if a <= x:
                x = a
            elif a <= y:
                y = a
            else:
                x == y
                y = a
                ans += 1
        
        print(ans)
        
    #State: `n` is an integer, `inp` is an empty list, `stdin` contains 0 inputs, `x` is the smallest element in the original list `inp`, `y` is the second smallest element in the original list `inp`, `ans` is the number of elements in the original list `inp` that are greater than the second smallest element, and the number of elements in the original list `inp` that are greater than the second smallest element is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer (array size) followed by a list of integers (array elements). It then finds the smallest and second smallest elements in the array, counts the number of elements greater than the second smallest element, and prints this count. The function repeats this process for all test cases in the input.

