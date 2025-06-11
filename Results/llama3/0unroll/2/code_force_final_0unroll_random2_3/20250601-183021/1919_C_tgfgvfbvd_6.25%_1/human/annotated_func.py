#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (the size of the array) and then a list of integers (the elements of the array). The size of the array is a positive integer and the elements of the array are positive integers less than or equal to the size of the array.
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        a = l[0]
        
        b = 0
        
        c = 0
        
        y = 0
        
        for y in range(1, n):
            if l[y] > l[y - 1]:
                b = l[y]
                break
        
        for x in range(y + 1, n):
            if l[x] > a and l[x] > b:
                if l[x] - a >= l[x] - b:
                    a = l[x]
                else:
                    b = l[x]
                c += 1
            elif l[x] < a and l[x] < b:
                if a - l[x] <= b - l[x]:
                    a = l[x]
                else:
                    b = l[x]
            elif a >= l[x]:
                a = l[x]
            else:
                b = l[x]
        
        print(c)
        
    #State: The output state will be the number of times the elements in the array are updated to maintain the conditions specified in the loop body. Specifically, it will be the number of times the variables 'a' and 'b' are updated to ensure that 'a' is the maximum element in the array and 'b' is the second maximum element in the array, or vice versa, while iterating through the array from the second element to the end.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of an integer array size and the array elements. It iterates through each array, maintaining two variables 'a' and 'b' to track the maximum and second maximum elements encountered so far, updating them according to specific conditions. The function outputs the number of updates made to 'a' and 'b' to ensure they represent the maximum and second maximum elements in the array, or vice versa.

