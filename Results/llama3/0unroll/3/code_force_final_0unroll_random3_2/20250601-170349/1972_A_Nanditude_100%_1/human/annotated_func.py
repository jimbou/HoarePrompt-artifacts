#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer, then two lists of integers of the same length as the first integer. The lists are sorted in non-decreasing order.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        b = list(map(int, input().split()))
        
        cnt = 0
        
        i = 0
        
        for j in range(n):
            if b[j] < a[i]:
                cnt += 1
            else:
                i += 1
        
        print(cnt)
        
    #State: The loop will execute t-1 times, and for each iteration, it will print the count of elements in list b that are less than the corresponding element in list a. The value of t will be 1, and the stdin will be empty.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer and two sorted lists of integers. It then compares the elements of the two lists and prints the count of elements in the second list that are less than the corresponding element in the first list. The function repeats this process for each test case and finally leaves the standard input empty.

