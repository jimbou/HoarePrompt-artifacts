#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (1 <= n <= 2 * 10^5) followed by n integers a_1, a_2, ..., a_n (-n <= a_i <= n).
    n = int(input())
    arr = list(map(int, input().split()))
    mex = []
    minn = 0
    maxx = 0
    for i in range(n):
        if arr[i] > 0:
            mex.append(minn)
            minn += 1
            if minn == maxx:
                minn = maxx + 1
        else:
            mex.append(abs(arr[i] - minn))
            if abs(arr[i] - minn) > maxx:
                maxx = abs(arr[i] - minn)
        
    #State: Output State: The output state after the loop executes all the iterations is: mex contains the minimum excluded value for each iteration, minn is the maximum value in mex plus one, and maxx is the maximum absolute value of the difference between the current element and minn.
    for itm in mex:
        print(itm, end=' ')
        
    #State: Output State: The output state after the loop executes all the iterations is: mex contains the minimum excluded value for each iteration, minn is the maximum value in mex plus one, and maxx is the maximum absolute value of the difference between the current element and minn.
    print()
    #This is printed: The minimum excluded value for each iteration, the maximum value in mex plus one, and the maximum absolute value of the difference between the current element and minn

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the minimum excluded value for each iteration. It accepts no parameters and returns no values. The input is expected to contain an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (1 <= n <= 2 * 10^5) followed by n integers a_1, a_2, ..., a_n (-n <= a_i <= n). The function processes each test case, calculating the minimum excluded value for each iteration, and prints these values separated by spaces. After processing all test cases, the function terminates.

