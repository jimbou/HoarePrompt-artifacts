#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing four integers p_i (0 <= p_i <= 200).
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] == a[1] == a[2] and a[0] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: cnt is the sum of the integer parts of all elements in a divided by 2, a is a list of four integers, x is the fourth element in a, stdin is empty, and cnt is printed

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of four integers. It calculates the sum of the integer parts of these integers divided by 2, with an additional increment if the first three integers are equal and odd. The function then prints this sum for each test case.

